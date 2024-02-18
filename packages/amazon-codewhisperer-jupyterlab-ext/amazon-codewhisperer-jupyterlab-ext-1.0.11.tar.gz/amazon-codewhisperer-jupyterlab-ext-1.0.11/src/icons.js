"use strict";
exports.__esModule = true;
exports.Icons = void 0;
/*!
 * Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
var ui_components_1 = require("@jupyterlab/ui-components");
var codewhisperer_svg_1 = require("../style/img/codewhisperer.svg");
var documentation_svg_1 = require("../style/img/documentation.svg");
var log_svg_1 = require("../style/img/log.svg");
var pause_svg_1 = require("../style/img/pause.svg");
var resume_svg_1 = require("../style/img/resume.svg");
var signout_svg_1 = require("../style/img/signout.svg");
var start_svg_1 = require("../style/img/start.svg");
var visual_cue_arrow_svg_1 = require("../style/img/visual-cue-arrow.svg");
var connected_svg_1 = require("../style/img/connected.svg");
var disconnected_svg_1 = require("../style/img/disconnected.svg");
var loading_svg_1 = require("../style/img/loading.svg");
// TODO: Update icons to be the 16x16 icon set
var Icons = /** @class */ (function () {
    function Icons() {
    }
    Icons.visualCueArrowIcon = new ui_components_1.LabIcon({
        name: 'visual-cue-arrow',
        svgstr: visual_cue_arrow_svg_1["default"]
    });
    Icons.logoIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:logo',
        svgstr: codewhisperer_svg_1["default"]
    });
    Icons.documentationIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:documentation',
        svgstr: documentation_svg_1["default"]
    });
    Icons.referenceLogIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:referenceLog',
        svgstr: log_svg_1["default"]
    });
    Icons.pauseIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:pause',
        svgstr: pause_svg_1["default"]
    });
    Icons.resumeIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:resume',
        svgstr: resume_svg_1["default"]
    });
    Icons.signOutIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:signOut',
        svgstr: signout_svg_1["default"]
    });
    Icons.startIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:start',
        svgstr: start_svg_1["default"]
    });
    Icons.connectedIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:connected',
        svgstr: connected_svg_1["default"]
    });
    Icons.disconnectedIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:disconnected',
        svgstr: disconnected_svg_1["default"]
    });
    Icons.loadingIcon = new ui_components_1.LabIcon({
        name: 'codewhisperer:loading',
        svgstr: loading_svg_1["default"]
    });
    return Icons;
}());
exports.Icons = Icons;
//# sourceMappingURL=icons.js.map