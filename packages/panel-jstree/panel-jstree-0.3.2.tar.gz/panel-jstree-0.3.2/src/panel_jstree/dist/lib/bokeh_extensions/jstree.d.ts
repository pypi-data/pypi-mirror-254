import * as p from "@bokehjs/core/properties";
import { HTMLBox, HTMLBoxView } from "./layout";
type Node = {
    [key: string]: any;
};
export declare class jsTreePlotView extends HTMLBoxView {
    model: jsTreePlot;
    protected _container: HTMLDivElement;
    protected _id: any;
    protected _jstree: any;
    protected _last_selected: string[];
    initialize(): void;
    connect_signals(): void;
    render(): void;
    init_callbacks(): void;
    onNewData(): void;
    selectNodeFromEditor({}: {}, data: any): void;
    _update_selection_from_value(): void;
    _update_tree_from_new_nodes(): void;
    _update_tree_from_data(): void;
    _setShowIcons(): void;
    _setShowDots(): void;
    setCheckboxes(): void;
    _setMultiple(): void;
    _update_tree_theme_from_model(): void;
    _listen_for_node_open({}: {}, data: any): void;
    add_node_children(node: Node): Node;
}
export declare namespace jsTreePlot {
    type Attrs = p.AttrsOf<Props>;
    type Props = HTMLBox.Props & {
        _data: p.Property<any>;
        plugins: p.Property<any>;
        checkbox: p.Property<boolean>;
        multiple: p.Property<boolean>;
        show_icons: p.Property<boolean>;
        show_dots: p.Property<boolean>;
        drag_and_drop: p.Property<boolean>;
        value: p.Property<any>;
        _last_opened: p.Property<any>;
        _new_nodes: p.Property<any>;
        _flat_tree: p.Property<any>;
    };
}
export interface jsTreePlot extends jsTreePlot.Attrs {
}
export declare class jsTreePlot extends HTMLBox {
    properties: jsTreePlot.Props;
    constructor(attrs?: Partial<jsTreePlot.Attrs>);
    static __module__: string;
}
export {};
