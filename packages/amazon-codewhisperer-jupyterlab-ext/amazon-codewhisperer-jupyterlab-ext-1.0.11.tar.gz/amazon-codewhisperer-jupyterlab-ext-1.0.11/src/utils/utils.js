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
exports.getErrorResponseUserMessage = exports.getResponseData = exports.isResponseSuccess = exports.removeState = exports.saveState = exports.loadState = exports.detectCompletionType = exports.sleep = exports.debouncePromise = void 0;
var application_1 = require("../application");
/**
 * @param f callback
 * @param wait milliseconds
 * @param abortValue if has abortValue, promise will reject it if
 * @returns Promise
 */
function debouncePromise(fn, wait, abortValue) {
    if (abortValue === void 0) { abortValue = undefined; }
    var cancel = function () {
        // do nothing
    };
    var wrapFunc = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        cancel();
        return new Promise(function (resolve, reject) {
            var timer = setTimeout(function () { return resolve(fn.apply(void 0, args)); }, wait);
            cancel = function () {
                clearTimeout(timer);
                if (abortValue !== undefined) {
                    reject(abortValue);
                }
            };
        });
    };
    return wrapFunc;
}
exports.debouncePromise = debouncePromise;
function sleep(duration) {
    if (duration === void 0) { duration = 0; }
    var schedule = setTimeout;
    return new Promise(function (r) { return schedule(r, Math.max(duration, 0)); });
}
exports.sleep = sleep;
function detectCompletionType(recommendations) {
    if (recommendations &&
        recommendations.length > 0) {
        if (recommendations[0].content.search("\n") !== -1) {
            return "Block";
        }
        else {
            return "Line";
        }
    }
    else {
        return undefined;
    }
}
exports.detectCompletionType = detectCompletionType;
// TODO: make loadState, saveState, removeState into Application as a centralized place to manage state
// Use `await loadState(id)` to get the actual value
function loadState(id) {
    return __awaiter(this, void 0, void 0, function () {
        var value, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 3, , 4]);
                    return [4 /*yield*/, application_1.Application.getInstance().stateDB.fetch(id)];
                case 1:
                    value = _a.sent();
                    return [4 /*yield*/, value];
                case 2: return [2 /*return*/, _a.sent()];
                case 3:
                    error_1 = _a.sent();
                    return [2 /*return*/, undefined];
                case 4: return [2 /*return*/];
            }
        });
    });
}
exports.loadState = loadState;
function saveState(id, value) {
    return __awaiter(this, void 0, void 0, function () {
        var error_2;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    return [4 /*yield*/, application_1.Application.getInstance().stateDB.save(id, value)];
                case 1:
                    _a.sent();
                    return [3 /*break*/, 3];
                case 2:
                    error_2 = _a.sent();
                    return [3 /*break*/, 3];
                case 3: return [2 /*return*/];
            }
        });
    });
}
exports.saveState = saveState;
function removeState(id) {
    return __awaiter(this, void 0, void 0, function () {
        var error_3;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    return [4 /*yield*/, application_1.Application.getInstance().stateDB.remove(id)];
                case 1:
                    _a.sent();
                    return [3 /*break*/, 3];
                case 2:
                    error_3 = _a.sent();
                    return [3 /*break*/, 3];
                case 3: return [2 /*return*/];
            }
        });
    });
}
exports.removeState = removeState;
function isResponseSuccess(json) {
    return json['status'] === 'SUCCESS';
}
exports.isResponseSuccess = isResponseSuccess;
function getResponseData(json) {
    return json['data'];
}
exports.getResponseData = getResponseData;
function getErrorResponseUserMessage(json) {
    if (json["error_info"]) {
        var errorInfo = json["error_info"];
        return errorInfo["user_message"];
    }
    else if (json["message"]) {
        return json["message"];
    }
    else {
        return "unknown error user message";
    }
}
exports.getErrorResponseUserMessage = getErrorResponseUserMessage;
//# sourceMappingURL=utils.js.map