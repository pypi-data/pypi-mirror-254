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
exports.Inline = void 0;
var worker_1 = require("../recommendation/worker");
var icons_1 = require("../icons");
var constants_1 = require("../utils/constants");
var autotrigger_1 = require("../autotrigger/autotrigger");
var recommendationStateHandler_1 = require("../recommendation/recommendationStateHandler");
var authManager_1 = require("../auth/authManager");
var referencetracker_1 = require("../referencetracker/referencetracker");
var extractor_1 = require("../recommendation/extractor");
var COMPLETER_ACTIVE_CLASS = 'jp-mod-inlinecompleter-active';
// TODO: The whole class needs to be refactored to utilize listeners/signals so we don't manually give instructions
// to manipulate inline UX everytime.
var Inline = /** @class */ (function () {
    function Inline() {
        this.completions = [];
        this.currentIndex = 0;
        this.typeahead = '';
        this.cursorObserver = undefined;
        this.invokeFileName = '';
        this.visualCueLeftMargin = 0;
    }
    Inline.getInstance = function () {
        if (!Inline.instance) {
            Inline.instance = new Inline();
        }
        return Inline.instance;
    };
    // TODO: refactor this into CSS
    Inline.prototype.getVisualCueHtmlElement = function () {
        var msg = document.createElement('span');
        var references = this.completions[this.currentIndex].references;
        msg.textContent = " Suggestion " + (this.currentIndex + 1) + " of " + this.completions.length + " from CodeWhisperer" + this.getReferenceLogMessage(references);
        msg.style.opacity = '0.60';
        msg.style.fontSize = this.invokeEditor.getOption('fontSize') - 1 + "px";
        msg.style.whiteSpace = "pre";
        msg.style.color = 'var(--jp-content-font-color1)';
        var icon = icons_1.Icons.visualCueArrowIcon.element();
        var iconSize = Math.max(this.invokeEditor.lineHeight - 4, 4);
        icon.style.width = iconSize + "px";
        icon.style.height = iconSize + "px";
        icon.style.opacity = '0.60';
        var visualCue = document.createElement('div');
        visualCue.style.display = 'flex';
        visualCue.style.alignItems = 'center';
        visualCue.appendChild(icon);
        visualCue.appendChild(msg);
        visualCue.className = 'InlineCompletionVisualCue';
        visualCue.style.backgroundColor = 'var(--jp-layout-color1)';
        return visualCue;
    };
    Inline.prototype.isCurrentFileJupyterNotebook = function () {
        return this.invokeEditor !== undefined && this.invokePanel !== undefined;
    };
    Inline.prototype.addOrUpdateVisualCue = function (left, top) {
        var _a;
        var newLeft = 0;
        if (this.visualCueWidget) {
            newLeft = Math.max(left + this.visualCueLeftMargin, parseFloat(this.visualCueWidget.style.left));
        }
        else {
            newLeft = left + this.visualCueLeftMargin;
        }
        var visualCueParent = undefined;
        if (this.isCurrentFileJupyterNotebook()) {
            // this is the parent element that allows visual cue to overflow and scroll
            // this parent contains the invokeEditor and a InputAreaPrompt to the left of invokeEditor
            // the left pixel needs to be adjusted due to the existence of InputAreaPrompt
            visualCueParent = this.invokeEditor.host.parentElement.parentElement.parentElement;
        }
        else {
            // for non notebook files, the parent has to be CodeMirror-lines to allow scrollable.
            visualCueParent = this.invokeEditor.host.parentElement.parentElement.querySelector('div.CodeMirror-lines');
        }
        this.setVisualCueLeftMargin();
        (_a = this.visualCueWidget) === null || _a === void 0 ? void 0 : _a.remove();
        this.visualCueWidget = this.getVisualCueHtmlElement();
        this.visualCueWidget.style.position = 'absolute';
        this.visualCueWidget.style.left = newLeft + "px";
        // since CodeMirror-lines does not allow overflow, only when invoking at the first line of non-notebook files
        // the visual Cue has to be at the bottom of ghost text
        if (!this.isCurrentFileJupyterNotebook() && this.invokeEditor.getCursorPosition().line === 0) {
            var lines = this.completions[this.currentIndex].content.split('\n').length;
            this.visualCueWidget.style.top = top + this.invokeEditor.lineHeight * lines + "px";
        }
        else {
            this.visualCueWidget.style.top = top - this.invokeEditor.lineHeight - 2 + "px";
        }
        // make sure the visual cue widget always shows on the top
        this.visualCueWidget.style.zIndex = '10';
        visualCueParent.appendChild(this.visualCueWidget);
    };
    Inline.prototype.setVisualCueLeftMargin = function () {
        if (this.visualCueLeftMargin === 0 && this.isCurrentFileJupyterNotebook()) {
            var inputAreaPromptHtmlElement = document.querySelector("jp-InputArea-prompt");
            if (inputAreaPromptHtmlElement) {
                // 16 is a constant gap between the input area prompt and editor
                this.visualCueLeftMargin = parseFloat(inputAreaPromptHtmlElement.style.width) + 16;
            }
            else {
                // 80px is the margin. This margin is not user configurable. It does not change when browser resizes
                this.visualCueLeftMargin = 80;
            }
        }
    };
    /* Widget for the inline completion ghost text
    */
    Inline.prototype.getElement = function (text) {
        var span = document.createElement('span');
        span.textContent = text;
        span.style.opacity = '0.70';
        span.className = 'cw-inline';
        var div = document.createElement('span');
        div.appendChild(span);
        return div;
    };
    Inline.prototype.getReferenceLogMessage = function (references) {
        if (references.length === 0) {
            return '';
        }
        var msg = ". Reference code under " + references[0].licenseName + ". View details in Reference logs.";
        return msg;
    };
    /* A function that detects whether a popup is active in the editor.
    */
    Inline.prototype.isPopupActive = function () {
        // completion popup
        var popup = document.querySelector(".jp-Notebook .jp-mod-completer-active");
        if (popup !== null) {
            return true;
        }
        // lsp hover 
        var lspTooltip = document.querySelector(".lsp-hover");
        if (lspTooltip !== null) {
            return true;
        }
        return false;
    };
    Inline.prototype.onReceiveListener = function (sender, value) {
        var _this = this;
        if (!this.invokeEditor) {
            this.removeCompletion();
            return;
        }
        else {
            if (this.completions.length === 0 && this.invokePosition) {
                // only update typeAheadLength if this is the first invocation
                var pos = this.invokeEditor.getCursorPosition();
                var cmEditor = this.invokeEditor;
                var newPos = { line: pos.line, ch: pos.column };
                var typeAheadOnFirstCompletion = cmEditor.getRange(this.invokePosition, newPos);
                recommendationStateHandler_1.RecommendationStateHandler.instance.typeAheadLength = typeAheadOnFirstCompletion.length;
            }
        }
        if (value.length > 0) {
            value.forEach(function (i) {
                if (i.content.length > 0) {
                    _this.completions.push(i);
                }
            });
        }
        if (this.isPopupActive()) {
            return;
        }
        // show first recommendation
        if (!this.isInlineSessionActive()) {
            if (this.completions.length === 0) {
                return;
            }
            var text = this.completions[0].content;
            this.currentIndex = 0;
            if (this.invokeEditor) {
                this.startShowCompletionTimer(text);
            }
        }
        else {
            // only refresh visual cue index
            var cmEditor = this.invokeEditor;
            // get the relative pixel position of the cursor in the CodeMirrorEditor
            var _a = cmEditor.cursorCoords(false, "local"), left = _a.left, top_1 = _a.top;
            this.setupVisualCueOnHover(left, top_1);
        }
    };
    Inline.prototype.startShowCompletionTimer = function (text) {
        var _this = this;
        if (this.showCompletionTimer) {
            return;
        }
        this.showCompletionTimer = setInterval(function () {
            var _a, _b, _c;
            var delay = performance.now() - autotrigger_1.AutoTrigger.getInstance().lastKeyStrokeTime;
            if (delay < constants_1.INLINE_COMPLETION_SHOW_DELAY) {
                return;
            }
            if (!_this.invokeEditor) {
                return;
            }
            try {
                var showed = _this.showCompletion(_this.invokeEditor, text);
                if (showed) {
                    // passing `this` so bind is not needed
                    (_a = _this.invokeEditor) === null || _a === void 0 ? void 0 : _a.model.selections.changed.connect(_this.onCursorChange, _this);
                    // make sure there is always one focus out event listener
                    (_b = _this.invokeEditor) === null || _b === void 0 ? void 0 : _b.host.removeEventListener('focusout', function () {
                        _this.onFocusOut();
                    });
                    (_c = _this.invokeEditor) === null || _c === void 0 ? void 0 : _c.host.addEventListener('focusout', function () {
                        _this.onFocusOut();
                    });
                }
            }
            finally {
                if (_this.showCompletionTimer) {
                    clearInterval(_this.showCompletionTimer);
                    _this.showCompletionTimer = undefined;
                }
            }
        }, constants_1.SHOW_COMPLETION_TIMER_POLL_PERIOD);
    };
    Inline.prototype.getCompletionsInNotebookPanel = function (panel, triggerMetadata) {
        var _a, _b;
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_c) {
                if (this.isInlineSessionActive()) {
                    return [2 /*return*/];
                }
                this.invokePanel = panel;
                this.invokeEditor = (_b = (_a = this.invokePanel) === null || _a === void 0 ? void 0 : _a.content.activeCell) === null || _b === void 0 ? void 0 : _b.editor;
                this.invokeFileName = this.invokePanel.context.path.split("/").pop();
                if (this.canInvokeRecommendation()) {
                    this.invokePosition = { line: this.invokeEditor.getCursorPosition().line, ch: this.invokeEditor.getCursorPosition().column };
                    worker_1.Worker.getInstance().getCompletionsPaginatedInNotebookPanel(panel, triggerMetadata);
                    worker_1.Worker.getInstance().receivedResponseSignal.connect(this.onReceiveListener, this);
                }
                return [2 /*return*/];
            });
        });
    };
    Inline.prototype.getCompletionsInEditor = function (editor, filename, triggerMetadata) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                if (this.isInlineSessionActive()) {
                    return [2 /*return*/];
                }
                this.invokeEditor = editor;
                this.invokeFileName = filename;
                if (this.canInvokeRecommendation()) {
                    this.invokePosition = { line: editor.getCursorPosition().line, ch: editor.getCursorPosition().column };
                    worker_1.Worker.getInstance().getCompletionsPaginatedInEditor(editor, filename, triggerMetadata);
                    worker_1.Worker.getInstance().receivedResponseSignal.connect(this.onReceiveListener, this);
                }
                return [2 /*return*/];
            });
        });
    };
    /* Returns a boolean that is true only when the current cursor exists but is not a selection
    */
    Inline.prototype.currentCursorIsNotASelection = function () {
        if (this.invokeEditor) {
            var selection = this.invokeEditor.getSelection();
            return selection.start.line === selection.end.line && selection.start.column === selection.end.column;
        }
        return false;
    };
    /* Can invoke only when in code cell in Jupyter Notebook and authenticated
    *  Do not invoke in non-python or non-Jupyter Notebook
    *  Only when current cursor is not a selection
    */
    Inline.prototype.canInvokeRecommendation = function () {
        if (worker_1.Worker.getInstance().isGetCompletionsRunning) {
            return false;
        }
        if (!authManager_1.AuthManager.getInstance().isAuthenticated()) {
            return false;
        }
        if (!(this.invokeFileName.endsWith('.py') || this.invokeFileName.endsWith('.ipynb'))) {
            return false;
        }
        if (this.invokePanel) {
            var cell = this.invokePanel.content.activeCell;
            if (extractor_1.isNotebookEmpty(this.invokePanel)) {
                return false;
            }
            return this.currentCursorIsNotASelection() && cell !== undefined && cell.model.type === "code";
        }
        else {
            return this.currentCursorIsNotASelection();
        }
    };
    Inline.prototype.onFocusOut = function () {
        this.removeCompletion();
    };
    Inline.prototype.showNext = function () {
        if (this.isInlineSessionActive()) {
            this.updateCurrentIndexNext();
            this.reloadSuggestionWidget();
        }
    };
    Inline.prototype.updateCurrentIndexNext = function () {
        for (var i = 0; i < this.completions.length; i++) {
            this.currentIndex = (this.currentIndex + 1) % this.completions.length;
            // we will only skip the current index and update it 
            // if the corresponding recommendation doesn't match typeahead
            if (this.completions[this.currentIndex].content.startsWith(this.typeahead)) {
                return;
            }
        }
    };
    Inline.prototype.updateCurrentIndexPrev = function () {
        for (var i = 0; i < this.completions.length; i++) {
            this.currentIndex = (this.completions.length + this.currentIndex - 1) % this.completions.length;
            // we will only skip the current index and update it 
            // if the corresponding recommendation doesn't match typeahead
            if (this.completions[this.currentIndex].content.startsWith(this.typeahead)) {
                return;
            }
        }
    };
    Inline.prototype.reloadSuggestionWidget = function () {
        var _a;
        (_a = this.marker) === null || _a === void 0 ? void 0 : _a.clear();
        var cmEditor = this.invokeEditor;
        var _b = cmEditor.cursorCoords(false, "local"), left = _b.left, top = _b.top;
        this.ghostTextWidget = this.getElement(this.completions[this.currentIndex].content.substring(this.typeahead.length));
        this.marker = cmEditor.doc.setBookmark(this.markerPosition, { widget: this.ghostTextWidget, insertLeft: true });
        this.setupVisualCueOnHover(left, top);
        recommendationStateHandler_1.RecommendationStateHandler.instance.setSuggestionState(this.currentIndex, "Showed");
        this.adjustCursorSizeAndPosition(this.invokeEditor);
    };
    /* By default, the visual cue shows on hover
    *  When there is code reference, visual cue always shows
    */
    Inline.prototype.setupVisualCueOnHover = function (left, top) {
        var _this = this;
        var _a;
        if (this.ghostTextWidget) {
            if (this.completions[this.currentIndex].references !== undefined && this.completions[this.currentIndex].references.length > 0) {
                this.addOrUpdateVisualCue(left, top);
            }
            else {
                (_a = this.visualCueWidget) === null || _a === void 0 ? void 0 : _a.remove();
                this.ghostTextWidget.addEventListener('mouseenter', function () {
                    _this.addOrUpdateVisualCue(left, top);
                });
                this.ghostTextWidget.addEventListener('mouseleave', function () {
                    var _a;
                    (_a = _this.visualCueWidget) === null || _a === void 0 ? void 0 : _a.remove();
                });
            }
        }
    };
    Inline.prototype.showPrev = function () {
        if (this.isInlineSessionActive()) {
            this.updateCurrentIndexPrev();
            this.reloadSuggestionWidget();
        }
    };
    Inline.prototype.onCursorChange = function () {
        if (this.invokeEditor && this.marker && this.invokePosition && this.ghostTextWidget) {
            var pos = this.invokeEditor.getCursorPosition();
            // Clear completion if the cursor is not at same line or it is on the left of typeahead
            if (pos.line !== this.invokePosition.line || (pos.column < this.invokePosition.ch + this.typeahead.length && pos.line === this.invokePosition.line)) {
                this.removeCompletion();
                return;
            }
            var cmEditor = this.invokeEditor;
            var newPos = { line: pos.line, ch: pos.column };
            this.typeahead = cmEditor.getRange(this.invokePosition, newPos);
            var text = this.completions[this.currentIndex].content;
            if (text.startsWith(this.typeahead)) {
                var _a = cmEditor.cursorCoords(false, "local"), left = _a.left, top_2 = _a.top;
                var newText = text.substring(this.typeahead.length);
                this.ghostTextWidget.querySelector("span.cw-inline").textContent = newText;
                this.setupVisualCueOnHover(left, top_2);
                this.markerPosition = newPos;
                this.adjustCursorSizeAndPosition(this.invokeEditor);
            }
            else {
                this.removeCompletion();
            }
        }
    };
    /* Shows a completion string in the Editor view
    *  Returns true if shows successfully, false otherwise
    */
    Inline.prototype.showCompletion = function (editor, text) {
        var _a, _b;
        var pos = editor.getCursorPosition();
        if (this.invokePosition === undefined) {
            this.removeCompletion();
            return false;
        }
        if (pos.line !== this.invokePosition.line || (pos.column < this.invokePosition.ch && pos.line === this.invokePosition.line)) {
            this.removeCompletion();
            return false;
        }
        var cmEditor = editor;
        if (!cmEditor.hasFocus()) {
            this.removeCompletion();
            return false;
        }
        var newPos = { line: pos.line, ch: pos.column };
        this.typeahead = cmEditor.getRange(this.invokePosition, newPos);
        if (text.startsWith(this.typeahead)) {
            var _c = cmEditor.cursorCoords(false, "local"), left = _c.left, top_3 = _c.top;
            this.ghostTextWidget = this.getElement(text.substring(this.typeahead.length));
            (_a = this.marker) === null || _a === void 0 ? void 0 : _a.clear();
            this.marker = cmEditor.doc.setBookmark(newPos, { widget: this.ghostTextWidget, insertLeft: true });
            this.markerPosition = newPos;
            (_b = this.invokeEditor) === null || _b === void 0 ? void 0 : _b.host.classList.add(COMPLETER_ACTIVE_CLASS);
            this.setupVisualCueOnHover(left, top_3);
            recommendationStateHandler_1.RecommendationStateHandler.instance.setSuggestionState(this.currentIndex, "Showed");
            this.adjustCursorSizeAndPosition(editor);
            return true;
        }
        else {
            this.removeCompletion();
            return false;
        }
    };
    /* This function resolves 2 bugs from CodeMirrorEditor
    * 1. Its cursor height can increase when there is a multi-line recommendation
    * 2. Its cursor left can move to leftmost of the line if ghost text is inserted right to non-whitespace characters.
    * 3. Its cursor top can move to the middle line of multi-line ghost text if ghost text is inserted right to non-whitespace characters in
    *    a non-Jupyter Notebook.
    */
    Inline.prototype.adjustCursorSizeAndPosition = function (editor) {
        var _this = this;
        var cursor = document.querySelector("div.CodeMirror-cursor");
        var cursorHeight = editor.lineHeight + "px";
        if (cursor) {
            cursor.style.height = cursorHeight;
            // when CodeMirror forces cursor to the left, use the correct logical position of JL Editor
            // to set the CSS of the cursor left pixels
            if (this.invokeEditor && parseFloat(cursor.style.left) < this.invokeEditor.charWidth) {
                var newLeft = parseFloat(cursor.style.left) + this.invokeEditor.getCursorPosition().column * this.invokeEditor.charWidth;
                cursor.style.left = newLeft + "px";
            }
            if (!this.isCurrentFileJupyterNotebook() && this.invokeEditor) {
                var cursorCssTop = parseFloat(cursor.style.top);
                var cursorLogicTop = this.invokeEditor.getCursorPosition().line * this.invokeEditor.lineHeight;
                if (cursorCssTop !== cursorLogicTop) {
                    cursor.style.top = cursorLogicTop + "px";
                }
            }
        }
        // Callback function to execute when CodeMirror cursor size overflows
        var callback = function (mutationList, observer) {
            for (var _i = 0, mutationList_1 = mutationList; _i < mutationList_1.length; _i++) {
                var mutation = mutationList_1[_i];
                if (mutation.type === "childList" && mutation.addedNodes.length > 0) {
                    var node = mutation.addedNodes[0];
                    if (node.className === "CodeMirror-cursor") {
                        if (node.style.height !== cursorHeight) {
                            node.style.height = cursorHeight;
                        }
                        // when CodeMirror forces cursor to the left, use the correct logical position of JL Editor
                        // to set the CSS of the cursor left pixels
                        if (_this.invokeEditor && parseFloat(node.style.left) < _this.invokeEditor.charWidth) {
                            var newLeft = parseFloat(node.style.left) + _this.invokeEditor.getCursorPosition().column * _this.invokeEditor.charWidth;
                            node.style.left = newLeft + "px";
                        }
                        if (!_this.isCurrentFileJupyterNotebook() && _this.invokeEditor) {
                            var cursorCssTop = parseFloat(cursor.style.top);
                            var cursorLogicTop = _this.invokeEditor.getCursorPosition().line * _this.invokeEditor.lineHeight;
                            if (cursorCssTop !== cursorLogicTop) {
                                cursor.style.top = cursorLogicTop + "px";
                            }
                        }
                    }
                }
            }
        };
        // Create an observer instance linked to the callback function
        this.cursorObserver = new MutationObserver(callback);
        this.cursorObserver.observe(document, { attributes: true, childList: true, subtree: true });
    };
    Inline.prototype.removeCompletion = function () {
        var _a, _b, _c, _d, _e;
        worker_1.Worker.getInstance().isInvocationCancelled = true;
        (_a = this.marker) === null || _a === void 0 ? void 0 : _a.clear();
        (_b = this.visualCueWidget) === null || _b === void 0 ? void 0 : _b.remove();
        this.visualCueWidget = undefined;
        this.visualCueLeftMargin = 0;
        (_c = this.invokeEditor) === null || _c === void 0 ? void 0 : _c.model.selections.changed.disconnect(this.onCursorChange, this);
        (_d = this.invokeEditor) === null || _d === void 0 ? void 0 : _d.host.classList.remove(COMPLETER_ACTIVE_CLASS);
        if (!worker_1.Worker.getInstance().isGetCompletionsRunning) {
            recommendationStateHandler_1.RecommendationStateHandler.instance.rejectRecommendationSignal.emit(-1);
        }
        (_e = this.cursorObserver) === null || _e === void 0 ? void 0 : _e.disconnect();
        this.cursorObserver = undefined;
        this.completions = [];
        this.currentIndex = 0;
        this.typeahead = '';
        this.invokePosition = undefined;
        this.markerPosition = undefined;
        this.ghostTextWidget = undefined;
        this.invokeEditor = undefined;
        this.invokePanel = undefined;
        this.invokeFileName = '';
        if (this.showCompletionTimer) {
            clearInterval(this.showCompletionTimer);
            this.showCompletionTimer = undefined;
        }
        this.forceClearGhostText();
    };
    // Sometimes the this.marker.clear() method
    // cannot remove the marker if user changes the Tab
    // this is the force clear the inline completion ghost text marker.
    Inline.prototype.forceClearGhostText = function () {
        return __awaiter(this, void 0, void 0, function () {
            var doc;
            return __generator(this, function (_a) {
                doc = document.querySelector('span.cw-inline');
                if (doc) {
                    doc.remove();
                }
                return [2 /*return*/];
            });
        });
    };
    Inline.prototype.isInlineSessionActive = function () {
        return this.invokeEditor !== undefined && this.ghostTextWidget !== undefined;
    };
    Inline.prototype.getCurrentSuggestionString = function () {
        var _a;
        var span = (_a = this.ghostTextWidget) === null || _a === void 0 ? void 0 : _a.querySelector('span.cw-inline');
        return span.textContent;
    };
    Inline.prototype.acceptCompletion = function (editor) {
        var _a;
        if (!this.isInlineSessionActive()) {
            return;
        }
        if (!editor) {
            editor = this.invokeEditor;
        }
        // this cursor change should not trigger the cursor change listener
        (_a = this.invokeEditor) === null || _a === void 0 ? void 0 : _a.model.selections.changed.disconnect(this.onCursorChange, this);
        var pos = editor.getCursorPosition();
        editor.setSelection({ start: pos, end: pos });
        editor.replaceSelection(this.getCurrentSuggestionString());
        worker_1.Worker.getInstance().isInvocationCancelled = true;
        recommendationStateHandler_1.RecommendationStateHandler.instance.acceptRecommendationSignal.emit(this.currentIndex);
        var references = this.completions[this.currentIndex].references;
        for (var _i = 0, references_1 = references; _i < references_1.length; _i++) {
            var reference = references_1[_i];
            var span = reference.recommendationContentSpan;
            var completion = this.completions[this.currentIndex].content;
            var referenceCode = completion.substring(span.start, span.end);
            // this.invokePosition is 0-indexed, hence line number is this.invokePosition + 1
            // #Lines in code snippet => completion.substring(0, span.start).split('\n').length - 1 as the array length will
            // one more than the number of lines in the snippet
            var startline = this.invokePosition.line + 1 + completion.substring(0, span.start).split('\n').length - 1;
            // End line is the start line + the number of lines in the snippet - 1 (exclude the last line)
            var endline = startline + (referenceCode.split('\n').length - 1) - 1;
            referencetracker_1.ReferenceTracker.getInstance().logReference(referenceCode, reference.licenseName, reference.repository, reference.url, this.invokeFileName, startline.toString(), endline.toString());
        }
        this.removeCompletion();
    };
    Inline.prototype.onEditorChange = function (editor) {
        this.removeCompletion();
    };
    return Inline;
}());
exports.Inline = Inline;
//# sourceMappingURL=inline.js.map