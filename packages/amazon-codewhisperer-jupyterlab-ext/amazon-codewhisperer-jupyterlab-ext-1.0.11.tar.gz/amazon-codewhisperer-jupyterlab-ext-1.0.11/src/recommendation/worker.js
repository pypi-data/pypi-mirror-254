"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
exports.Worker = void 0;
var apiclient_1 = require("../client/apiclient");
var extractor_1 = require("./extractor");
var constants_1 = require("../utils/constants");
var messages_1 = require("../messages");
var signaling_1 = require("@lumino/signaling");
var logger_1 = require("../logging/logger");
var notifications_1 = require("../notifications/notifications");
var utils_1 = require("../utils/utils");
var recommendationStateHandler_1 = require("./recommendationStateHandler");
var Worker = /** @class */ (function () {
    function Worker() {
        this._isGetCompletionsRunning = false;
        /**
         * This boolean is used to stop subsequent paginated requests when user has rejected/accepted
         * any completions returned by previous requests.
         */
        this.isInvocationCancelled = false;
        this.optOut = false;
        this.client = new apiclient_1.ApiClient();
        this.receivedResponseSignal = new signaling_1.Signal(this);
        this.serviceInvocationSignal = new signaling_1.Signal(this);
        this.invocationStatusChangedSignal = new signaling_1.Signal(this);
        this.logger = logger_1.Logger.getInstance({
            "name": "codewhisperer",
            "component": "worker"
        });
    }
    Worker.getInstance = function () {
        if (!Worker.instance) {
            Worker.instance = new Worker();
        }
        return Worker.instance;
    };
    Object.defineProperty(Worker.prototype, "isGetCompletionsRunning", {
        get: function () {
            return this._isGetCompletionsRunning;
        },
        set: function (value) {
            this._isGetCompletionsRunning = value;
            this.invocationStatusChangedSignal.emit(value);
        },
        enumerable: false,
        configurable: true
    });
    /* Call the generateCompletions API with next Token and emit result
     *  this.isGetCompletionsRunning is used to ensure concurrency <= 1
     */
    Worker.prototype.getCompletionsPaginated = function (request, triggerMetadata, fileContextMetadata) {
        return __awaiter(this, void 0, void 0, function () {
            var responseJson, requestId, sessionId, credentialStartUrl, page, startTime, reason, result, recommendationCount, shouldRecordServiceInvocation, response, error_1, errUserMessage, recommendations, completionType;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        responseJson = undefined;
                        requestId = "";
                        sessionId = "";
                        credentialStartUrl = "";
                        page = 0;
                        startTime = undefined;
                        reason = undefined;
                        result = undefined;
                        recommendationCount = 0;
                        shouldRecordServiceInvocation = true;
                        if (this._isGetCompletionsRunning) {
                            return [2 /*return*/];
                        }
                        recommendationStateHandler_1.RecommendationStateHandler.instance.rejectRecommendationSignal.emit(-1);
                        this.isInvocationCancelled = false;
                        _a.label = 1;
                    case 1:
                        if (!(!this.isInvocationCancelled && page < constants_1.MAX_PAGINATION_CALLS)) return [3 /*break*/, 10];
                        this.isGetCompletionsRunning = true;
                        _a.label = 2;
                    case 2:
                        _a.trys.push([2, 5, 6, 9]);
                        startTime = Date.now();
                        return [4 /*yield*/, this.client.generateRecommendations(request, this.optOut)];
                    case 3:
                        response = _a.sent();
                        return [4 /*yield*/, response.json()];
                    case 4:
                        responseJson = _a.sent();
                        this.logger.debug("responseJson", responseJson);
                        requestId = responseJson["x-amzn-requestid"];
                        sessionId = responseJson["x-amzn-sessionid"];
                        result = "Succeeded";
                        return [3 /*break*/, 9];
                    case 5:
                        error_1 = _a.sent();
                        this.logger.error("Error in calling generateRecommendations API ", error_1);
                        reason = error_1;
                        result = "Failed";
                        return [3 /*break*/, 9];
                    case 6:
                        if (!(responseJson && !utils_1.isResponseSuccess(responseJson))) return [3 /*break*/, 8];
                        errUserMessage = utils_1.getErrorResponseUserMessage(responseJson);
                        return [4 /*yield*/, notifications_1.NotificationManager.getInstance().postNotificationForApiExceptions(errUserMessage, messages_1.message("codewhisperer_learn_more"), constants_1.LEARN_MORE_NOTIFICATION_URL)];
                    case 7:
                        _a.sent();
                        reason = errUserMessage;
                        if (responseJson["message"] && responseJson["message"].includes("Invalid input data")) {
                            shouldRecordServiceInvocation = false;
                            this.logger.debug("Invalid input data, not recording service invocation");
                        }
                        result = "Failed";
                        _a.label = 8;
                    case 8:
                        recommendations = undefined;
                        if (responseJson && utils_1.isResponseSuccess(responseJson)) {
                            if ("recommendations" in responseJson["data"]) {
                                recommendations = responseJson["data"].recommendations;
                            }
                            else if ("completions" in responseJson["data"]) {
                                recommendations = responseJson["data"].completions;
                                credentialStartUrl = constants_1.AWS_BUILDER_ID_START_URL;
                            }
                            if (!this.suggestionsWithCodeReferences) {
                                recommendations = recommendations.filter(function (r) { return !Array.isArray(r.references) || r.references.length === 0; });
                            }
                        }
                        if (recommendations) {
                            this.receivedResponseSignal.emit(recommendations);
                            recommendationCount += recommendations.length > 0 ? recommendations.length : 1;
                            this.logger.debug("successfully received valid recommendations");
                        }
                        completionType = utils_1.detectCompletionType(recommendations);
                        if (shouldRecordServiceInvocation) {
                            this.serviceInvocationSignal.emit({
                                codewhispererRequestId: requestId,
                                credentialStartUrl: credentialStartUrl,
                                duration: Date.now() - startTime,
                                reason: reason,
                                result: result,
                                codewhispererCompletionType: completionType,
                                codewhispererTriggerType: triggerMetadata.triggerType,
                                codewhispererAutomatedTriggerType: triggerMetadata.automatedTriggerType,
                                codewhispererSessionId: sessionId,
                                // TODO: sessionID, runtime and runtimeSource
                                codewhispererJupyterLabCellCount: fileContextMetadata.cellCount,
                                codewhispererJupyterLabCellIndex: fileContextMetadata.activeCellIdx,
                                codewhispererJupyterLabCellType: fileContextMetadata.cellType,
                                codewhispererLanguage: triggerMetadata.language,
                                codewhispererLastSuggestionIndex: (result === "Succeeded" && recommendations) ? recommendationCount - 1 : -1,
                                codewhispererCursorOffset: fileContextMetadata.cursorOffset,
                                codewhispererLineNumber: fileContextMetadata.lineNumber,
                            });
                        }
                        if (result === "Succeeded") {
                            recommendationStateHandler_1.RecommendationStateHandler.instance.updateInvocationMetadata({
                                completionType: completionType,
                                credentialStartUrl: credentialStartUrl,
                                sessionId: sessionId,
                                paginationProgress: recommendationCount,
                                fileContextMetadata: fileContextMetadata,
                                triggerMetadata: triggerMetadata
                            }, requestId, page === 0);
                            if (recommendations) {
                                recommendationStateHandler_1.RecommendationStateHandler.instance.addRecommendations(recommendations);
                            }
                        }
                        if (responseJson && utils_1.isResponseSuccess(responseJson) && responseJson['data'].nextToken !== '') {
                            request.nextToken = responseJson['data'].nextToken;
                        }
                        else {
                            return [3 /*break*/, 10];
                        }
                        page++;
                        return [7 /*endfinally*/];
                    case 9: return [3 /*break*/, 1];
                    case 10:
                        if (this.isInvocationCancelled) {
                            recommendationStateHandler_1.RecommendationStateHandler.instance.rejectRecommendationSignal.emit(-1);
                        }
                        this.isGetCompletionsRunning = false;
                        return [2 /*return*/];
                }
            });
        });
    };
    Worker.prototype.getCompletionsPaginatedInNotebookPanel = function (panel, triggerMetadata) {
        return __awaiter(this, void 0, void 0, function () {
            var _a, fileContext, fileContextMetadata, request;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        _a = extractor_1.getFileContextFromNotebook(panel), fileContext = _a.fileContext, fileContextMetadata = _a.fileContextMetadata;
                        request = {
                            fileContext: fileContext,
                            maxResults: constants_1.MAX_RECOMMENDATIONS,
                            referenceTrackerConfiguration: {
                                recommendationsWithReferences: this.suggestionsWithCodeReferences ? "ALLOW" : "BLOCK",
                            },
                            nextToken: "",
                        };
                        return [4 /*yield*/, this.getCompletionsPaginated(request, triggerMetadata, fileContextMetadata)];
                    case 1: return [2 /*return*/, _b.sent()];
                }
            });
        });
    };
    Worker.prototype.getCompletionsPaginatedInEditor = function (editor, filename, triggerMetadata) {
        return __awaiter(this, void 0, void 0, function () {
            var _a, fileContext, fileContextMetadata, request;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0:
                        _a = extractor_1.getFileContextFromEditor(editor, filename), fileContext = _a.fileContext, fileContextMetadata = _a.fileContextMetadata;
                        request = {
                            fileContext: fileContext,
                            maxResults: constants_1.MAX_RECOMMENDATIONS,
                            referenceTrackerConfiguration: {
                                recommendationsWithReferences: "ALLOW",
                            },
                            nextToken: "",
                        };
                        return [4 /*yield*/, this.getCompletionsPaginated(request, triggerMetadata, fileContextMetadata)];
                    case 1:
                        _b.sent();
                        return [2 /*return*/];
                }
            });
        });
    };
    Worker.prototype.setSuggestionsWithCodeReferences = function (suggestionsWithCodeReferences) {
        this.suggestionsWithCodeReferences = suggestionsWithCodeReferences;
    };
    Worker.prototype.isSuggestionsWithCodeReferencesEnabled = function () {
        return this.suggestionsWithCodeReferences;
    };
    Worker.prototype.setOptOut = function (optOut) {
        this.optOut = optOut;
    };
    return Worker;
}());
exports.Worker = Worker;
//# sourceMappingURL=worker.js.map