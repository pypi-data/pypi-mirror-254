"use strict";
exports.__esModule = true;
exports.SettingIDs = exports.HttpStatusCode = exports.MESSAGE_TO_CMD_ID_MAP = exports.PLUGIN_ID = exports.CommandIDs = exports.NOTIFICATION_TEXT_LIMIT = exports.NEW_CELL_AUTO_TRIGGER_DELAY_IN_MS = exports.SHOW_COMPLETION_TIMER_POLL_PERIOD = exports.INLINE_COMPLETION_SHOW_DELAY = exports.AWS_BUILDER_ID_START_URL = exports.MAX_PAGINATION_CALLS = exports.MAX_RECOMMENDATIONS = exports.MAX_LENGTH = exports.CWSPR_DOCUMENTATION = exports.UPDATE_NOTIFICATION_URL = exports.LEARN_MORE_NOTIFICATION_URL = exports.TELEMETRY_USER_TRIGGER_DECISION_METRIC_NAME = exports.TELEMETRY_USER_DECISION_METRIC_NAME = exports.TELEMETRY_SERVICE_INVOCATION_METRIC_NAME = void 0;
/**
 * The metric name that will be used to send telemetry event data.
 */
exports.TELEMETRY_SERVICE_INVOCATION_METRIC_NAME = "codewhisperer_serviceInvocation";
exports.TELEMETRY_USER_DECISION_METRIC_NAME = "codewhisperer_userDecision";
exports.TELEMETRY_USER_TRIGGER_DECISION_METRIC_NAME = "codewhisperer_userTriggerDecision";
exports.LEARN_MORE_NOTIFICATION_URL = "https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html";
// TODO : Update this to CodeWhisperer URL after finalizing name
exports.UPDATE_NOTIFICATION_URL = "https://pypi.org/project/amazon-codewhisperer-jupyterlab-ext/";
exports.CWSPR_DOCUMENTATION = "https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html";
exports.MAX_LENGTH = 10240;
exports.MAX_RECOMMENDATIONS = 5;
exports.MAX_PAGINATION_CALLS = 10;
exports.AWS_BUILDER_ID_START_URL = "https://view.awsapps.com/start";
//  delay in ms when showing suggestion before user last keystroke input
exports.INLINE_COMPLETION_SHOW_DELAY = 250;
// the poll period of show completion timer in ms
exports.SHOW_COMPLETION_TIMER_POLL_PERIOD = 25;
exports.NEW_CELL_AUTO_TRIGGER_DELAY_IN_MS = 10000;
exports.NOTIFICATION_TEXT_LIMIT = 140;
/**
 * The command IDs used by the console plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.invoke = 'completer:invoke';
    CommandIDs.invokeNotebook = 'completer:invoke-notebook';
    CommandIDs.invokeFile = 'completer:invoke-file';
    CommandIDs.select = 'completer:select';
    CommandIDs.selectNotebook = 'completer:select-notebook';
    CommandIDs.login = 'codewhisperer:login';
    CommandIDs.invokeInline = 'codewhisperer:invoke-inline';
    CommandIDs.rejectInline = 'codewhisperer:reject-inline';
    CommandIDs.acceptInline = 'codewhisperer:accept-inline';
    CommandIDs.showNext = 'codewhisperer:show-next';
    CommandIDs.showPrev = 'codewhisperer:show-prev';
    CommandIDs.startCodeWhisperer = 'codewhisperer:start';
    CommandIDs.cancelLogin = 'codewhisperer:cancel-login';
    CommandIDs.openDocumentation = 'codewhisperer:documentation';
    CommandIDs.pauseAutoSuggestion = 'codewhisperer:pause-auto-suggestion';
    CommandIDs.resumeAutoSuggestion = 'codewhisperer:resume-auto-suggestion';
    CommandIDs.openReferenceLog = 'codewhisperer:open-reference-log';
    CommandIDs.signOut = 'codewhisperer:sign-out';
    CommandIDs.keyShortcutTitle = 'codewhisperer:key-shortcut-title';
    CommandIDs.keyShortcutAccept = 'codewhisperer:key-shortcut-accept';
    CommandIDs.keyShortcutManualTrigger = 'codewhisperer:key-shortcut-manual-trigger';
    CommandIDs.keyShortcutNavigate = 'codewhisperer:key-shortcut-navigate';
    CommandIDs.keyShortcutReject = 'codewhisperer:key-shortcut-reject';
    CommandIDs.toggleTelemetry = 'codewhisperer:toggle-telemetry';
    CommandIDs.toggleCodeReferences = 'codewhisperer:toggle-code-references';
})(CommandIDs = exports.CommandIDs || (exports.CommandIDs = {}));
exports.PLUGIN_ID = 'amazon-codewhisperer-jupyterlab-ext:completer';
exports.MESSAGE_TO_CMD_ID_MAP = {
    "codewhisperer_key_shortcut_accept": CommandIDs.acceptInline,
    "codewhisperer_key_shortcut_manual_trigger": CommandIDs.invokeInline,
    "codewhisperer_key_shortcut_reject": CommandIDs.rejectInline,
};
var HttpStatusCode;
(function (HttpStatusCode) {
    HttpStatusCode[HttpStatusCode["OK"] = 200] = "OK";
    HttpStatusCode[HttpStatusCode["NOT_FOUND"] = 404] = "NOT_FOUND";
})(HttpStatusCode = exports.HttpStatusCode || (exports.HttpStatusCode = {}));
var SettingIDs;
(function (SettingIDs) {
    SettingIDs.keyOptOut = 'shareCodeWhispererContentWithAWS';
    SettingIDs.keyTelemetry = 'codeWhispererTelemetry';
    SettingIDs.keyReferences = 'suggestionsWithCodeReferences';
    SettingIDs.keyLogLevel = 'codeWhispererLogLevel';
})(SettingIDs = exports.SettingIDs || (exports.SettingIDs = {}));
//# sourceMappingURL=constants.js.map