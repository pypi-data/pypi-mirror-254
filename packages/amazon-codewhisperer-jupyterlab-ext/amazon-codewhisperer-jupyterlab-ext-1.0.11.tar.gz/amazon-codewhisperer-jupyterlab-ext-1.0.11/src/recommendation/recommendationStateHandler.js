"use strict";
var __classPrivateFieldGet = (this && this.__classPrivateFieldGet) || function (receiver, state, kind, f) {
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a getter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot read private member from an object whose class did not declare it");
    return kind === "m" ? f : kind === "a" ? f.call(receiver) : f ? f.value : state.get(receiver);
};
var __classPrivateFieldSet = (this && this.__classPrivateFieldSet) || function (receiver, state, value, kind, f) {
    if (kind === "m") throw new TypeError("Private method is not writable");
    if (kind === "a" && !f) throw new TypeError("Private accessor was defined without a setter");
    if (typeof state === "function" ? receiver !== state || !f : !state.has(receiver)) throw new TypeError("Cannot write private member to an object whose class did not declare it");
    return (kind === "a" ? f.call(receiver, value) : f ? f.value = value : state.set(receiver, value)), value;
};
var _a, _RecommendationStateHandler_instance;
exports.__esModule = true;
exports.RecommendationStateHandler = void 0;
var telemetry_1 = require("../telemetry/telemetry");
var constants_1 = require("../utils/constants");
var licenseUtils_1 = require("../utils/licenseUtils");
var signaling_1 = require("@lumino/signaling");
var logger_1 = require("../logging/logger");
var RecommendationStateHandler = /** @class */ (function () {
    function RecommendationStateHandler() {
        this.acceptedIndex = -1;
        this.timeSinceLastUserDecision = undefined;
        this.timeSinceLastDocumentChange = undefined;
        this.recommendations = [];
        this.recommendationSuggestionState = new Map();
        this.acceptRecommendationSignal = new signaling_1.Signal(this);
        this.acceptRecommendationSignal.connect(this.userDecisionSignalListener, this);
        this.rejectRecommendationSignal = new signaling_1.Signal(this);
        this.rejectRecommendationSignal.connect(this.userDecisionSignalListener, this);
        this.logger = logger_1.Logger.getInstance({
            "name": "codewhisperer",
            "component": "recommendationStateHandler"
        });
    }
    RecommendationStateHandler.prototype.reset = function () {
        this.timeToFirstRecommendation = undefined;
        this.requestId = undefined;
        this.firstRequestId = undefined;
        this.invocationMetadata = undefined;
        this.acceptedIndex = -1;
        this.recommendations = [];
        this.recommendationSuggestionState = new Map();
        return;
    };
    Object.defineProperty(RecommendationStateHandler, "instance", {
        get: function () {
            var _b;
            return (__classPrivateFieldSet(this, _a, (_b = __classPrivateFieldGet(this, _a, "f", _RecommendationStateHandler_instance)) !== null && _b !== void 0 ? _b : new this(), "f", _RecommendationStateHandler_instance));
        },
        enumerable: false,
        configurable: true
    });
    RecommendationStateHandler.prototype.updateInvocationMetadata = function (invocationMetadata, requestId, isFirstInvocation) {
        if (isFirstInvocation) {
            // first invocation
            this.invocationMetadata = invocationMetadata;
            this.firstRequestId = requestId;
            this.requestId = requestId;
            this.timeToFirstRecommendation = performance.now() - invocationMetadata.triggerMetadata.triggerTime;
        }
        else {
            // subsequent invocation
            this.requestId = requestId;
        }
    };
    RecommendationStateHandler.prototype.setSuggestionState = function (index, value) {
        this.logger.debug("setSuggestionState: index: " + index + " value: " + value);
        this.recommendationSuggestionState.set(index, value);
    };
    RecommendationStateHandler.prototype.addRecommendations = function (recommendations) {
        this.updateRecommendationState(recommendations);
    };
    RecommendationStateHandler.prototype.addRecommendation = function (recommendation) {
        this.recommendations.push(recommendation);
    };
    RecommendationStateHandler.prototype.updateRecommendationState = function (recommendations) {
        var previousRecommendationsLength = this.recommendations.length;
        if (recommendations.length > 0) {
            recommendations.forEach(function (recommendation, index) {
                // value: RecommendationsList is appended to this.completions, so the index of the current completion is the length of this.completions - 1
                RecommendationStateHandler.instance.setSuggestionState(previousRecommendationsLength + index, "Discard");
                RecommendationStateHandler.instance.addRecommendation(recommendation);
            });
        }
        else {
            RecommendationStateHandler.instance.addRecommendation({ content: "", references: [] });
            RecommendationStateHandler.instance.setSuggestionState(previousRecommendationsLength, "Empty");
        }
        ;
    };
    RecommendationStateHandler.prototype.userDecisionSignalListener = function (sender, value) {
        this.acceptedIndex = value;
        this.recordUserDecisionTelemetry();
    };
    RecommendationStateHandler.prototype.recordUserDecisionTelemetry = function () {
        var _this = this;
        if (!this.invocationMetadata) {
            //TODO: this is not the optimal solution. 
            // We should record suggestions as Discard for the ones returned after user moves
            // on from (accept/reject) the previous suggestions
            this.reset();
            return;
        }
        var userDecisionEvents = [];
        this.recommendations.forEach(function (recommendation, index) {
            var _b;
            var uniqueSuggestionReferences = undefined;
            var uniqueLicenseSet = licenseUtils_1.LicenseUtil.getUniqueLicenseNames(recommendation.references);
            if (uniqueLicenseSet.size > 0) {
                uniqueSuggestionReferences = JSON.stringify(Array.from(uniqueLicenseSet));
            }
            if (recommendation.content.length === 0) {
                (_b = _this.recommendationSuggestionState) === null || _b === void 0 ? void 0 : _b.set(index, "Empty");
            }
            var event = {
                codewhispererSuggestionIndex: index,
                codewhispererSuggestionState: _this.getSuggestionState(index, _this.acceptedIndex),
                codewhispererCompletionType: _this.invocationMetadata.completionType,
                codewhispererLanguage: _this.invocationMetadata.triggerMetadata.language,
                codewhispererSessionId: _this.invocationMetadata.sessionId,
                codewhispererRequestId: _this.requestId,
                codewhispererPaginationProgress: _this.invocationMetadata.paginationProgress,
                codewhispererSuggestionReferences: uniqueSuggestionReferences,
                codewhispererSuggestionReferenceCount: recommendation.references
                    ? recommendation.references.length
                    : 0,
                credentialStartUrl: _this.invocationMetadata.credentialStartUrl,
                codewhispererTriggerType: _this.invocationMetadata.triggerMetadata.triggerType,
            };
            userDecisionEvents.push(event);
            telemetry_1.Telemetry.getInstance().recordTelemetry(constants_1.TELEMETRY_USER_DECISION_METRIC_NAME, event);
        });
        this.recordUserTriggerDecisionTelemetry(userDecisionEvents);
        this.reset();
    };
    RecommendationStateHandler.prototype.recordUserTriggerDecisionTelemetry = function (events) {
        if (!this.invocationMetadata) {
            return;
        }
        var userDecisionByTrigger = this.getAggregatedUserDecisionBySession(events);
        var event = {
            codewhispererSessionId: this.invocationMetadata.sessionId,
            codewhispererFirstRequestId: this.firstRequestId,
            codewhispererSuggestionState: userDecisionByTrigger,
            codewhispererCompletionType: this.invocationMetadata.completionType,
            codewhispererTriggerType: this.invocationMetadata.triggerMetadata.triggerType,
            codewhispererLanguage: this.invocationMetadata.triggerMetadata.language,
            codewhispererAutomatedTriggerType: this.invocationMetadata.triggerMetadata.automatedTriggerType,
            codewhispererLineNumber: this.invocationMetadata.fileContextMetadata.lineNumber,
            codewhispererCursorOffset: this.invocationMetadata.fileContextMetadata.cursorOffset,
            codewhispererJupyterLabCellCount: this.invocationMetadata.fileContextMetadata.cellCount,
            codewhispererJupyterLabCellIndex: this.invocationMetadata.fileContextMetadata.activeCellIdx,
            codewhispererJupyterLabCellType: this.invocationMetadata.fileContextMetadata.cellType,
            codewhispererSuggestionCount: this.recommendations.length,
            codewhispererTriggerCharacter: this.invocationMetadata.triggerMetadata.triggerType === 'AutoTrigger' ? this.invocationMetadata.triggerMetadata.triggerCharacter : undefined,
            codewhispererPreviousSuggestionState: this.previousSuggestionState,
            codewhispererTimeToFirstRecommendation: this.timeToFirstRecommendation,
            codewhispererTimeSinceLastUserDecision: this.timeSinceLastUserDecision ? performance.now() - this.timeSinceLastUserDecision : undefined,
            codewhispererTimeSinceLastDocumentChange: this.timeSinceLastDocumentChange,
            codewhispererTypeaheadLength: this.typeAheadLength,
            codewhispererSuggestionImportCount: undefined, // This is dummy value, we don't have this available in JupyterLab at the moment
        };
        telemetry_1.Telemetry.getInstance().recordTelemetry(constants_1.TELEMETRY_USER_TRIGGER_DECISION_METRIC_NAME, event);
        this.previousSuggestionState = userDecisionByTrigger;
    };
    RecommendationStateHandler.prototype.getSuggestionState = function (i, acceptIndex) {
        var _b;
        var state = (_b = this.recommendationSuggestionState) === null || _b === void 0 ? void 0 : _b.get(i);
        if (state && acceptIndex === -1 && ["Empty", "Filter", "Discard"].includes(state)) {
            return state;
        }
        else if (this.recommendationSuggestionState !== undefined &&
            this.recommendationSuggestionState.get(i) !== "Showed") {
            return "Unseen";
        }
        if (acceptIndex === -1) {
            return "Reject";
        }
        return i === acceptIndex ? "Accept" : "Ignore";
    };
    /**
     * 1. if there is any Accept within the session, mark the session as Accept.
     * 2. if there is any Reject within the session, mark the session as Reject.
     * 3. if all recommendations within the session are empty, mark the session as Empty.
     *
     * @returns the aggregated user decision by session.
     */
    RecommendationStateHandler.prototype.getAggregatedUserDecisionBySession = function (events) {
        var isEmpty = true;
        for (var _i = 0, events_1 = events; _i < events_1.length; _i++) {
            var event_1 = events_1[_i];
            if (event_1.codewhispererSuggestionState === 'Accept') {
                return 'Accept';
            }
            else if (event_1.codewhispererSuggestionState === 'Reject') {
                return 'Reject';
            }
            else if (event_1.codewhispererSuggestionState !== 'Empty') {
                isEmpty = false;
            }
        }
        return isEmpty ? 'Empty' : 'Discard';
    };
    return RecommendationStateHandler;
}());
exports.RecommendationStateHandler = RecommendationStateHandler;
_a = RecommendationStateHandler;
_RecommendationStateHandler_instance = { value: void 0 };
//# sourceMappingURL=recommendationStateHandler.js.map