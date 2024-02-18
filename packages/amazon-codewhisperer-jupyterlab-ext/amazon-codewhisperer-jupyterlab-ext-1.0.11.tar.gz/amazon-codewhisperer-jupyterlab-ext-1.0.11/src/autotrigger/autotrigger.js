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
exports.AutoTrigger = void 0;
var inline_1 = require("../inline/inline");
var logger_1 = require("../logging/logger");
var recommendationStateHandler_1 = require("../recommendation/recommendationStateHandler");
var utils_1 = require("../utils/utils");
var application_1 = require("../application");
var stateKeys_1 = require("../utils/stateKeys");
// TODO: Too many states maintained, only enabled is needed
var AutoTrigger = /** @class */ (function () {
    function AutoTrigger() {
        this.specialCharacters = new Set(['(', '[', ':', '{']);
        this.lastKeyStrokeTime = 0;
        this._registeredEditors = [];
        this.enabled = true;
        this.logger = logger_1.Logger.getInstance({
            "name": "codewhisperer",
            "component": "autotrigger"
        });
        application_1.Application.getInstance().loadStateSignal.connect(this.loadState, this);
    }
    AutoTrigger.getInstance = function () {
        if (!AutoTrigger.instance) {
            AutoTrigger.instance = new AutoTrigger();
        }
        return AutoTrigger.instance;
    };
    AutoTrigger.prototype.loadState = function (sender) {
        return __awaiter(this, void 0, void 0, function () {
            var isAutoSuggestionEnabled;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, utils_1.loadState(stateKeys_1.AUTO_SUGGESTION)
                        // isAutoSuggestionEnabled is undefined if stateDB object is not init with the AUTO_SUGGESTION key
                    ];
                    case 1:
                        isAutoSuggestionEnabled = _a.sent();
                        // isAutoSuggestionEnabled is undefined if stateDB object is not init with the AUTO_SUGGESTION key
                        this.enabled = isAutoSuggestionEnabled === undefined || isAutoSuggestionEnabled;
                        return [2 /*return*/];
                }
            });
        });
    };
    Object.defineProperty(AutoTrigger.prototype, "isAutoSuggestionEnabled", {
        get: function () {
            return this.enabled;
        },
        set: function (value) {
            this.enabled = value;
        },
        enumerable: false,
        configurable: true
    });
    AutoTrigger.prototype.registerListener = function (editor, panel, filename) {
        var _this = this;
        if (this._registeredEditors.includes(editor)) {
            return;
        }
        var changeHandler = function (sender, args) { return __awaiter(_this, void 0, void 0, function () {
            var now, _a, autoTriggerType, triggerCharacter;
            return __generator(this, function (_b) {
                now = performance.now();
                recommendationStateHandler_1.RecommendationStateHandler.instance.timeSinceLastDocumentChange = now - this.lastKeyStrokeTime;
                if (!this.enabled) {
                    this.lastKeyStrokeTime = now;
                    return [2 /*return*/];
                }
                _a = this.shouldAutoTrigger(args), autoTriggerType = _a.autoTriggerType, triggerCharacter = _a.triggerCharacter;
                this.invokeAutoTrigger(editor, panel, autoTriggerType, triggerCharacter, this.lastKeyStrokeTime);
                this.lastKeyStrokeTime = now;
                return [2 /*return*/];
            });
        }); };
        changeHandler = changeHandler.bind(this);
        editor.model.value.changed.connect(changeHandler);
        // OK if the editors/cells are removed later, they will just be stale copies and be cleaned on next IDE restart
        this._registeredEditors.push(editor);
        this.filename = filename;
    };
    AutoTrigger.prototype.onSwitchToNewCell = function (editor, panel) {
        if (!this.enabled) {
            return;
        }
        var cell = panel.content.activeCell;
        if (cell.model.type === 'code' && editor.getCursorPosition().line === 0
            && editor.getCursorPosition().column === 0
            && editor.model.value.text.trim().length === 0) {
            this.invokeAutoTrigger(editor, panel, "NewCell", undefined, this.lastKeyStrokeTime);
        }
    };
    AutoTrigger.prototype.invokeAutoTrigger = function (editor, panel, autoTriggerType, triggerCharacter, triggerTime) {
        this.logger.debug("invokeAutoTrigger - " + autoTriggerType + " - " + triggerCharacter + " - " + triggerTime);
        if (autoTriggerType) {
            if (panel) {
                // invoke in a Notebook panel
                inline_1.Inline.getInstance().getCompletionsInNotebookPanel(panel, {
                    triggerCharacter: triggerCharacter,
                    triggerTime: triggerTime,
                    automatedTriggerType: autoTriggerType,
                    triggerType: "AutoTrigger",
                    language: "ipynb"
                });
            }
            else if (editor) {
                // invoke in python file
                inline_1.Inline.getInstance().getCompletionsInEditor(editor, this.filename, {
                    triggerCharacter: triggerCharacter,
                    triggerTime: triggerTime,
                    automatedTriggerType: autoTriggerType,
                    triggerType: "AutoTrigger",
                    language: "python"
                });
            }
        }
        else {
            this.logger.debug("Not Valid auto trigger character");
        }
    };
    AutoTrigger.prototype.shouldAutoTrigger = function (changeArgs) {
        var autoTriggerType = undefined;
        var triggerCharacter = undefined;
        autoTriggerType = this.changeIsNewLine(changeArgs);
        if (!autoTriggerType) {
            autoTriggerType = this.changeIsSpecialCharacter(changeArgs).autoTriggerType;
            triggerCharacter = this.changeIsSpecialCharacter(changeArgs).triggerCharacter;
            if (!autoTriggerType) {
                autoTriggerType = this.changeIsIdleTimeTrigger(changeArgs);
            }
        }
        return { autoTriggerType: autoTriggerType, triggerCharacter: triggerCharacter };
    };
    AutoTrigger.prototype.changeIsNewLine = function (changeArgs) {
        var shouldTrigger = (changeArgs.type === 'insert' && changeArgs.value.trim() === '' && changeArgs.value.startsWith('\n'));
        if (shouldTrigger) {
            return "Enter";
        }
        else {
            return undefined;
        }
    };
    AutoTrigger.prototype.changeIsSpecialCharacter = function (changeArgs) {
        var shouldTrigger = (changeArgs.type === 'insert' && this.specialCharacters.has(changeArgs.value));
        if (shouldTrigger) {
            return { autoTriggerType: "SpecialCharacters", triggerCharacter: changeArgs.value };
        }
        else {
            return { autoTriggerType: undefined, triggerCharacter: undefined };
        }
    };
    AutoTrigger.prototype.changeIsIdleTimeTrigger = function (changeArgs) {
        var shouldTrigger = (performance.now() - this.lastKeyStrokeTime >= 2000 && changeArgs.type === 'insert');
        if (shouldTrigger) {
            return "IdleTime";
        }
        else {
            return undefined;
        }
    };
    return AutoTrigger;
}());
exports.AutoTrigger = AutoTrigger;
//# sourceMappingURL=autotrigger.js.map