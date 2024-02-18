"use strict";
exports.__esModule = true;
exports.LicenseUtil = void 0;
var LicenseUtil = /** @class */ (function () {
    function LicenseUtil() {
    }
    LicenseUtil.getUniqueLicenseNames = function (references) {
        var n = new Set();
        references === null || references === void 0 ? void 0 : references.forEach(function (r) {
            if (r.licenseName) {
                n.add(r.licenseName);
            }
        });
        return n;
    };
    return LicenseUtil;
}());
exports.LicenseUtil = LicenseUtil;
//# sourceMappingURL=licenseUtils.js.map