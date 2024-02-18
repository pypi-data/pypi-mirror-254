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
exports.Application = void 0;
/*!
 * Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
var signaling_1 = require("@lumino/signaling");
var autotrigger_1 = require("./autotrigger/autotrigger");
var worker_1 = require("./recommendation/worker");
var authManager_1 = require("./auth/authManager");
var handler_1 = require("./handler");
var utils_1 = require("./utils/utils");
var constants_1 = require("./utils/constants");
var notifications_1 = require("./notifications/notifications");
var constants_2 = require("./utils/constants");
var messages_1 = require("./messages");
var Application = /** @class */ (function () {
    function Application() {
        this._environment = undefined;
        this.loadStateSignal = new signaling_1.Signal(this);
        this.toggleSettingSignal = new signaling_1.Signal(this);
    }
    Application.getInstance = function () {
        if (!Application.instance) {
            Application.instance = new Application();
        }
        return Application.instance;
    };
    Application.prototype._fetchEnvironment = function () {
        return __awaiter(this, void 0, void 0, function () {
            var getEnvironmentResponse, getEnvironmentResponseJson, versionNotification, latestVersion;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, handler_1.requestAPI('get_environment')];
                    case 1:
                        getEnvironmentResponse = _a.sent();
                        if (getEnvironmentResponse.status !== constants_1.HttpStatusCode.OK)
                            return [2 /*return*/];
                        return [4 /*yield*/, getEnvironmentResponse.json()];
                    case 2:
                        getEnvironmentResponseJson = _a.sent();
                        this._environment = utils_1.getResponseData(getEnvironmentResponseJson)['environment'];
                        versionNotification = utils_1.getResponseData(getEnvironmentResponseJson)['version_notification'];
                        latestVersion = utils_1.getResponseData(getEnvironmentResponseJson)['latest_version'];
                        if (versionNotification) {
                            notifications_1.NotificationManager.getInstance().postNotificationForUpdateInformation(versionNotification, latestVersion, messages_1.message("codewhisperer_update_now"), constants_2.UPDATE_NOTIFICATION_URL).then();
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    Application.prototype.isJupyterOSS = function () {
        return this._environment === Environment.JUPYTER_OSS;
    };
    Application.prototype.isSageMakerStudio = function () {
        return this._environment === Environment.SM_STUDIO;
    };
    Application.prototype.isGlueStudioNoteBook = function () {
        return this._environment === Environment.GLUE_STUDIO_NOTEBOOK;
    };
    // Initialize all the application singletons here
    Application.prototype.loadServices = function (stateDB, jupyterApp) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        this.stateDB = stateDB;
                        this.jupyterApp = jupyterApp;
                        return [4 /*yield*/, this._fetchEnvironment()];
                    case 1:
                        _a.sent();
                        worker_1.Worker.getInstance();
                        autotrigger_1.AutoTrigger.getInstance();
                        authManager_1.AuthManager.getInstance();
                        return [2 /*return*/];
                }
            });
        });
    };
    return Application;
}());
exports.Application = Application;
var Environment;
(function (Environment) {
    Environment["JUPYTER_OSS"] = "Jupyter OSS";
    Environment["SM_STUDIO"] = "SageMaker Studio";
    Environment["GLUE_STUDIO_NOTEBOOK"] = "Glue Studio Notebook";
})(Environment || (Environment = {}));
//# sourceMappingURL=application.js.map