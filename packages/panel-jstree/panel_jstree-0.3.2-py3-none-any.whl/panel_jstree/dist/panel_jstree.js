/*!
 * Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 * 
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * 
 * Neither the name of Anaconda nor the names of any contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */
(function(root, factory) {
  factory(root["Bokeh"], undefined);
})(this, function(Bokeh, version) {
  let define;
  return (function(modules, entry, aliases, externals) {
    const bokeh = typeof Bokeh !== "undefined" && (version != null ? Bokeh[version] : Bokeh);
    if (bokeh != null) {
      return bokeh.register_plugin(modules, entry, aliases);
    } else {
      throw new Error("Cannot find Bokeh " + version + ". You have to load it prior to loading plugins.");
    }
  })
({
"ecf49f9c64": /* index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const tslib_1 = require("tslib");
    // export {jsTreePlot} from "./models/jstree"
    // import {register_models} from "@bokehjs/base"
    // register_models(jsTreePlot as any)
    const PaneljsTree = tslib_1.__importStar(require("ef403b5ad2") /* ./bokeh_extensions/ */);
    exports.PaneljsTree = PaneljsTree;
    const base_1 = require("@bokehjs/base");
    (0, base_1.register_models)(PaneljsTree);
},
"ef403b5ad2": /* bokeh_extensions/index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const tslib_1 = require("tslib");
    const jsTree = tslib_1.__importStar(require("15032009db") /* ./jstree */);
    exports.jsTree = jsTree;
    const base_1 = require("@bokehjs/base");
    (0, base_1.register_models)(jsTree);
},
"15032009db": /* bokeh_extensions/jstree.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    var _a;
    const dom_1 = require("@bokehjs/core/dom");
    const layout_1 = require("bfe8e8c0eb") /* ./layout */;
    function ID() {
        // Math.random should be unique because of its seeding algorithm.
        // Convert it to base 36 (numbers + letters), and grab the first 9 characters
        // after the decimal.
        return '_' + Math.random().toString(36).substring(2, 11);
    }
    class jsTreePlotView extends layout_1.HTMLBoxView {
        initialize() {
            super.initialize();
            this._last_selected = [];
        }
        connect_signals() {
            console.log("connect");
            super.connect_signals();
            this.connect(this.model.properties._data.change, () => this._update_tree_from_data());
            this.connect(this.model.properties.value.change, () => this._update_selection_from_value());
            this.connect(this.model.properties._new_nodes.change, () => this._update_tree_from_new_nodes());
            this.connect(this.model.properties.checkbox.change, () => this.setCheckboxes());
            this.connect(this.model.properties.show_icons.change, () => this._setShowIcons());
            this.connect(this.model.properties.show_dots.change, () => this._setShowDots());
            this.connect(this.model.properties.multiple.change, () => this._setMultiple());
            console.log(this.model.show_dots);
            console.log(this.model.show_icons);
        }
        render() {
            super.render();
            this._id = ID();
            console.log(this._id);
            this._container = (0, dom_1.div)({ id: this._id, style: "overflow: auto; minHeight: 200px; minWidth: 200px;" });
            (0, layout_1.set_size)(this._container, this.model);
            this.shadow_el.appendChild(this._container);
            console.log(this._container);
            let kw = { "checkbox": {
                    "three_state": false,
                    "cascade": "undetermined"
                } };
            if (this.model.checkbox) {
                this.model.plugins.push("checkbox");
            }
            if (this.model.drag_and_drop) {
                this.model.plugins.push("dnd");
                kw["check_callback"] = true;
            }
            this._jstree = jQuery(this._container).jstree(Object.assign({ "core": { "data": this.model._data, "check_callback": true,
                    "multiple": this.model.multiple,
                    "themes": {
                        "dots": this.model.show_dots,
                        "icons": this.model.show_icons
                    }
                }, "plugins": this.model.plugins }, kw));
            this.init_callbacks();
        }
        init_callbacks() {
            // Initialization
            // Rendering callbacks
            // TODO: do I need both of these?
            this._jstree.on('refresh.jstree', ({}, {}) => this._update_selection_from_value());
            // Sync state with model
            this._jstree.on('model.jstree', ({}, {}) => this.onNewData());
            this._jstree.on('activate_node.jstree', ({}, data) => this.selectNodeFromEditor({}, data));
            this._jstree.on('before_open.jstree', (e, data) => this._listen_for_node_open(e, data));
        }
        onNewData() {
            this.model._flat_tree = this._jstree.jstree(true).get_json(null, { "flat": true });
            console.log("flat tree: ", this.model._flat_tree);
        }
        selectNodeFromEditor({}, data) {
            console.log("select pre", this.model.value);
            this.model.value = data.instance.get_selected();
            console.log("select post", this.model.value);
        }
        _update_selection_from_value() {
            console.log("update selection from value");
            this._jstree.jstree(true).select_node(this.model.value);
            // We sometimes have to fire this function more than once per value change because of
            // calling jstree.refresh, so we check to see if model.value has really changed
            // by comparing to last_selected
            if (this.model.value != this._last_selected) {
                let deselected = this._last_selected.filter(x => !this.model.value.includes(x));
                this._jstree.jstree(true).deselect_node(deselected);
            }
            // We choose get_selected
            this._last_selected = this.model.value;
        }
        _update_tree_from_new_nodes() {
            console.log("new nodes: ", this.model._new_nodes);
            for (let node of this.model._new_nodes) {
                this._jstree.jstree(true).create_node(node["parent"], node, "first");
            }
            this._jstree.jstree(true).settings.core.data = this._jstree.jstree(true).get_json(null, { no_li_attr: true, no_a_attr: true, no_data: true });
            this.model._data = this._jstree.jstree(true).settings.core.data;
            // this._update_selection_from_value()
        }
        _update_tree_from_data() {
            console.log("updating data");
            this._jstree.jstree(true).settings.core.data = this.model._data;
            console.log("data: ", this._jstree.jstree(true).settings.core.data);
            console.log("value after data", this.model.value);
            // This will redraw the tree if we swap out the data with new data
            // we set forget_state to true, so the current state is not reapplied
            // letting whatever state is set in the new data (open or closed, etc)
            // be the new state
            this._jstree.jstree(true).refresh({ "skip_loading": false,
                "forget_state": true });
            // selected state is not preserved correctly right now, so we then
            // deselect everything because that is better than getting it wrong
            this._jstree.jstree(true).deselect_all({ "supress_event": true });
            console.log("value after refresh", this.model.value);
            console.log("data after refresh", this._jstree.jstree(true).settings.core.data);
        }
        _setShowIcons() {
            console.log("setShowIcons");
            if (this.model.show_icons) {
                this._jstree.jstree(true).show_icons();
            }
            else {
                this._jstree.jstree(true).hide_icons();
            }
        }
        _setShowDots() {
            console.log("setShowDots");
            if (this.model.show_dots) {
                this._jstree.jstree(true).show_dots();
            }
            else {
                this._jstree.jstree(true).hide_dots();
            }
        }
        setCheckboxes() {
            console.log("setCheckBoxes");
            if (this.model.checkbox) {
                this._jstree.jstree(true).show_checkboxes();
            }
            else {
                this._jstree.jstree(true).hide_checkboxes();
            }
        }
        _setMultiple() {
            console.log("setMultiple");
            this._jstree.jstree(true).settings.core.multiple = this.model.multiple;
        }
        _update_tree_theme_from_model() {
            this._jstree.jstree(true).refresh(false, true);
        }
        _listen_for_node_open({}, data) {
            console.log("listen for node open");
            data.node = this.add_node_children(data.node);
            this.model._last_opened = data.node;
        }
        add_node_children(node) {
            console.log("add node children");
            node["children_nodes"] = [];
            for (let child of node.children) {
                node.children_nodes.push(this._jstree.jstree(true).get_node(child));
            }
            return node;
        }
    }
    exports.jsTreePlotView = jsTreePlotView;
    jsTreePlotView.__name__ = "jsTreePlotView";
    class jsTreePlot extends layout_1.HTMLBox {
        constructor(attrs) {
            super(attrs);
        }
    }
    exports.jsTreePlot = jsTreePlot;
    _a = jsTreePlot;
    jsTreePlot.__name__ = "jsTreePlot";
    jsTreePlot.__module__ = "panel_jstree.bokeh_extensions.jstree";
    (() => {
        _a.prototype.default_view = jsTreePlotView;
        _a.define(({ Array, Any, Boolean }) => ({
            value: [Array(Any), []],
            _data: [Array(Any), []],
            plugins: [Array(Any), []],
            checkbox: [Boolean, true],
            multiple: [Boolean, true],
            show_icons: [Boolean, true],
            show_dots: [Boolean, true],
            drag_and_drop: [Boolean, false],
            _last_opened: [Any, {}],
            _new_nodes: [Array(Any), []],
            _flat_tree: [Array(Any), []],
        }));
    })();
},
"bfe8e8c0eb": /* bokeh_extensions/layout.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const dom_1 = require("@bokehjs/core/dom");
    const types_1 = require("@bokehjs/core/util/types");
    const widget_1 = require("@bokehjs/models/widgets/widget");
    const layout_dom_1 = require("@bokehjs/models/layouts/layout_dom");
    class PanelMarkupView extends widget_1.WidgetView {
        async lazy_initialize() {
            await super.lazy_initialize();
            if (this.provider.status == "not_started" || this.provider.status == "loading")
                this.provider.ready.connect(() => {
                    if (this.contains_tex_string(this.model.text))
                        this.render();
                });
        }
        connect_signals() {
            super.connect_signals();
            this.connect(this.model.change, () => {
                this.render();
            });
        }
        has_math_disabled() {
            return this.model.disable_math || !this.contains_tex_string(this.model.text);
        }
        render() {
            super.render();
            set_size(this.el, this.model);
            this.container = (0, dom_1.div)();
            set_size(this.container, this.model, false);
            this.shadow_el.appendChild(this.container);
            if (this.provider.status == "failed" || this.provider.status == "loaded")
                this._has_finished = true;
        }
    }
    exports.PanelMarkupView = PanelMarkupView;
    PanelMarkupView.__name__ = "PanelMarkupView";
    function set_size(el, model, adjustMargin = true) {
        let width_policy = model.width != null ? "fixed" : "fit";
        let height_policy = model.height != null ? "fixed" : "fit";
        const { sizing_mode, margin } = model;
        if (sizing_mode != null) {
            if (sizing_mode == "fixed")
                width_policy = height_policy = "fixed";
            else if (sizing_mode == "stretch_both")
                width_policy = height_policy = "max";
            else if (sizing_mode == "stretch_width")
                width_policy = "max";
            else if (sizing_mode == "stretch_height")
                height_policy = "max";
            else {
                switch (sizing_mode) {
                    case "scale_width":
                        width_policy = "max";
                        height_policy = "min";
                        break;
                    case "scale_height":
                        width_policy = "min";
                        height_policy = "max";
                        break;
                    case "scale_both":
                        width_policy = "max";
                        height_policy = "max";
                        break;
                    default:
                        throw new Error("unreachable");
                }
            }
        }
        let wm, hm;
        if (!adjustMargin) {
            hm = wm = 0;
        }
        else if ((0, types_1.isArray)(margin)) {
            if (margin.length === 4) {
                hm = margin[0] + margin[2];
                wm = margin[1] + margin[3];
            }
            else {
                hm = margin[0] * 2;
                wm = margin[1] * 2;
            }
        }
        else if (margin == null) {
            hm = wm = 0;
        }
        else {
            wm = hm = margin * 2;
        }
        if (width_policy == "fixed" && model.width)
            el.style.width = model.width + "px";
        else if (width_policy == "max")
            el.style.width = wm ? `calc(100% - ${wm}px)` : "100%";
        if (model.min_width != null)
            el.style.minWidth = model.min_width + "px";
        if (model.max_width != null)
            el.style.maxWidth = model.max_width + "px";
        if (height_policy == "fixed" && model.height)
            el.style.height = model.height + "px";
        else if (height_policy == "max")
            el.style.height = hm ? `calc(100% - ${hm}px)` : "100%";
        if (model.min_height != null)
            el.style.minHeight = model.min_height + "px";
        if (model.max_width != null)
            el.style.maxHeight = model.max_height + "px";
    }
    exports.set_size = set_size;
    class HTMLBoxView extends layout_dom_1.LayoutDOMView {
        render() {
            super.render();
            set_size(this.el, this.model);
        }
        watch_stylesheets() {
            this._initialized_stylesheets = {};
            for (const sts of this._applied_stylesheets) {
                const style_el = sts.el;
                if (style_el instanceof HTMLLinkElement) {
                    this._initialized_stylesheets[style_el.href] = false;
                    style_el.addEventListener("load", () => {
                        this._initialized_stylesheets[style_el.href] = true;
                        if (Object.values(this._initialized_stylesheets).every(Boolean))
                            this.style_redraw();
                    });
                }
            }
        }
        style_redraw() {
        }
        get child_models() {
            return [];
        }
    }
    exports.HTMLBoxView = HTMLBoxView;
    HTMLBoxView.__name__ = "HTMLBoxView";
    class HTMLBox extends layout_dom_1.LayoutDOM {
        constructor(attrs) {
            super(attrs);
        }
    }
    exports.HTMLBox = HTMLBox;
    HTMLBox.__name__ = "HTMLBox";
},
}, "ecf49f9c64", {"index":"ecf49f9c64","bokeh_extensions/index":"ef403b5ad2","bokeh_extensions/jstree":"15032009db","bokeh_extensions/layout":"bfe8e8c0eb"}, {});});
//# sourceMappingURL=panel_jstree.js.map
