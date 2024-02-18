"use strict";
exports.__esModule = true;
exports.getFileContextFromEditor = exports.getFileContextFromNotebook = exports.isNotebookEmpty = void 0;
var logger_1 = require("../logging/logger");
var constants_1 = require("../utils/constants");
var logger = logger_1.Logger.getInstance({
    "name": "codewhisperer",
    "component": "extractor"
});
/* This function serialized a notebook cell
* For markdown cell, convert it into python comment per line
* For code cell, send it as it is
* Add a \n between each cell
* Add one more \n after markdown cell, this is to let model know markdown has finished.
*/
function encodeCell(cell) {
    if (cell.type === 'code') {
        return cell.toJSON()['source'] + '\n';
    }
    else if (cell.type === 'markdown') {
        var src = cell.toJSON()['source'];
        var lines = [];
        if (Array.isArray(src)) {
            lines = src;
        }
        else {
            lines = src.split('\n');
        }
        return '# ' + lines.join('\n# ') + '\n\n';
    }
    return "";
}
function isNotebookEmpty(panel) {
    var cells = panel.content.model.cells;
    for (var i = 0; i < cells.length; i++) {
        var cell = cells.get(i);
        var src = cell.toJSON()['source'];
        if (src.trim() !== '') {
            return false;
        }
    }
    return true;
}
exports.isNotebookEmpty = isNotebookEmpty;
function getFileContextFromNotebook(panel) {
    var _a;
    var notebook = panel.content;
    var activeCell = notebook.activeCell;
    var editor = (_a = notebook.activeCell) === null || _a === void 0 ? void 0 : _a.editor;
    var cellCount = notebook.model.cells.length;
    var cellType = activeCell.model.type;
    var lineNumber = editor === null || editor === void 0 ? void 0 : editor.getCursorPosition().line;
    var cursorOffset = editor === null || editor === void 0 ? void 0 : editor.getOffsetAt(editor.getCursorPosition());
    var fileContext = undefined;
    if (editor && activeCell) {
        var cells = notebook.model.cells;
        var left = "";
        var right = "";
        for (var i = 0; i < cells.length; i++) {
            var cell = cells.get(i);
            if (i < notebook.activeCellIndex) {
                left += encodeCell(cell);
            }
            else if (i === notebook.activeCellIndex) {
                var pos = editor.getCursorPosition();
                var offset = editor.getOffsetAt(pos);
                var text = editor.model.value.text;
                left += text.substring(0, offset);
                right += text.substring(offset, text.length);
            }
            else {
                right += encodeCell(cell);
            }
        }
        logger.debug("Notebook content length - left:" + left.slice.length + " right:" + left.slice.length);
        fileContext = {
            leftFileContent: left.slice(-constants_1.MAX_LENGTH),
            rightFileContent: right.slice(0, constants_1.MAX_LENGTH),
            filename: panel.context.path.split("/").pop(),
            programmingLanguage: {
                languageName: "python",
            }
        };
    }
    return {
        fileContext: fileContext,
        fileContextMetadata: {
            activeCellIdx: notebook.activeCellIndex,
            cellCount: cellCount,
            cellType: cellType,
            lineNumber: lineNumber,
            cursorOffset: cursorOffset,
        }
    };
}
exports.getFileContextFromNotebook = getFileContextFromNotebook;
function getFileContextFromEditor(editor, filename) {
    var fileContext = undefined;
    var pos = undefined;
    var offset = undefined;
    if (editor) {
        pos = editor.getCursorPosition();
        offset = editor.getOffsetAt(pos);
        var text = editor.model.value.text;
        var left = text.substring(0, offset);
        var right = text.substring(offset, text.length);
        logger.debug("File content length - left:" + left.slice.length + " right:" + left.slice.length);
        fileContext = {
            leftFileContent: left.slice(-constants_1.MAX_LENGTH),
            rightFileContent: right.slice(0, constants_1.MAX_LENGTH),
            filename: filename,
            programmingLanguage: {
                languageName: "python",
            },
        };
    }
    return {
        fileContext: fileContext,
        fileContextMetadata: {
            lineNumber: pos.line,
            cursorOffset: offset,
        }
    };
}
exports.getFileContextFromEditor = getFileContextFromEditor;
//# sourceMappingURL=extractor.js.map