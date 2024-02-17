const {
  SvelteComponent: m,
  append: g,
  attr: r,
  detach: v,
  element: f,
  init: o,
  insert: y,
  noop: u,
  safe_not_equal: b,
  src_url_equal: d,
  toggle_class: _
} = window.__gradio__svelte__internal;
function h(s) {
  let e, t, i;
  return {
    c() {
      var l;
      e = f("div"), t = f("img"), d(t.src, i = /*samples_dir*/
      s[1] + /*value*/
      ((l = s[0]) == null ? void 0 : l.path)) || r(t, "src", i), r(t, "alt", ""), r(e, "class", "container svelte-wo3k18"), _(
        e,
        "table",
        /*type*/
        s[2] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        s[2] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        s[3]
      );
    },
    m(l, a) {
      y(l, e, a), g(e, t);
    },
    p(l, [a]) {
      var c;
      a & /*samples_dir, value*/
      3 && !d(t.src, i = /*samples_dir*/
      l[1] + /*value*/
      ((c = l[0]) == null ? void 0 : c.path)) && r(t, "src", i), a & /*type*/
      4 && _(
        e,
        "table",
        /*type*/
        l[2] === "table"
      ), a & /*type*/
      4 && _(
        e,
        "gallery",
        /*type*/
        l[2] === "gallery"
      ), a & /*selected*/
      8 && _(
        e,
        "selected",
        /*selected*/
        l[3]
      );
    },
    i: u,
    o: u,
    d(l) {
      l && v(e);
    }
  };
}
function w(s, e, t) {
  let { value: i } = e, { samples_dir: l } = e, { type: a } = e, { selected: c = !1 } = e;
  return s.$$set = (n) => {
    "value" in n && t(0, i = n.value), "samples_dir" in n && t(1, l = n.samples_dir), "type" in n && t(2, a = n.type), "selected" in n && t(3, c = n.selected);
  }, [i, l, a, c];
}
class q extends m {
  constructor(e) {
    super(), o(this, e, w, h, b, {
      value: 0,
      samples_dir: 1,
      type: 2,
      selected: 3
    });
  }
}
export {
  q as default
};
