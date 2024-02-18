const { setContext: D, getContext: g } = window.__gradio__svelte__internal, h = "WORKER_PROXY_CONTEXT_KEY";
function w() {
  return g(h);
}
function y(n) {
  return n.host === window.location.host || n.host === "localhost:7860" || n.host === "127.0.0.1:7860" || // Ref: https://github.com/gradio-app/gradio/blob/v3.32.0/js/app/src/Index.svelte#L194
  n.host === "lite.local";
}
function b(n, e) {
  const r = e.toLowerCase();
  for (const [s, l] of Object.entries(n))
    if (s.toLowerCase() === r)
      return l;
}
function p(n) {
  if (n == null)
    return !1;
  const e = new URL(n);
  return !(!y(e) || e.protocol !== "http:" && e.protocol !== "https:");
}
async function v(n) {
  if (n == null || !p(n))
    return n;
  const e = w();
  if (e == null)
    return n;
  const s = new URL(n).pathname;
  return e.httpRequest({
    method: "GET",
    path: s,
    headers: {},
    query_string: ""
  }).then((l) => {
    if (l.status !== 200)
      throw new Error(`Failed to get file ${s} from the Wasm worker.`);
    const t = new Blob([l.body], {
      type: b(l.headers, "content-type")
    });
    return URL.createObjectURL(t);
  });
}
const {
  SvelteComponent: R,
  assign: c,
  compute_rest_props: u,
  detach: C,
  element: E,
  exclude_internal_props: O,
  get_spread_update: q,
  init: L,
  insert: U,
  noop: f,
  safe_not_equal: k,
  set_attributes: m,
  src_url_equal: K
} = window.__gradio__svelte__internal;
function P(n) {
  let e, r, s = [
    {
      src: r = /*resolved_src*/
      n[0]
    },
    /*$$restProps*/
    n[1]
  ], l = {};
  for (let t = 0; t < s.length; t += 1)
    l = c(l, s[t]);
  return {
    c() {
      e = E("img"), m(e, l);
    },
    m(t, o) {
      U(t, e, o);
    },
    p(t, [o]) {
      m(e, l = q(s, [
        o & /*resolved_src*/
        1 && !K(e.src, r = /*resolved_src*/
        t[0]) && { src: r },
        o & /*$$restProps*/
        2 && /*$$restProps*/
        t[1]
      ]));
    },
    i: f,
    o: f,
    d(t) {
      t && C(e);
    }
  };
}
function T(n, e, r) {
  const s = ["src"];
  let l = u(e, s), { src: t = void 0 } = e, o, a;
  return n.$$set = (i) => {
    e = c(c({}, e), O(i)), r(1, l = u(e, s)), "src" in i && r(2, t = i.src);
  }, n.$$.update = () => {
    if (n.$$.dirty & /*src, latest_src*/
    12) {
      r(0, o = t), r(3, a = t);
      const i = t;
      v(i).then((d) => {
        a === i && r(0, o = d);
      });
    }
  }, [o, l, t, a];
}
class W extends R {
  constructor(e) {
    super(), L(this, e, T, P, k, { src: 2 });
  }
}
const {
  SvelteComponent: X,
  attr: Y,
  create_component: S,
  destroy_component: j,
  detach: x,
  element: N,
  init: B,
  insert: F,
  mount_component: G,
  safe_not_equal: H,
  toggle_class: _,
  transition_in: I,
  transition_out: V
} = window.__gradio__svelte__internal;
function z(n) {
  var l;
  let e, r, s;
  return r = new W({
    props: {
      src: (
        /*samples_dir*/
        n[1] + /*value*/
        ((l = n[0]) == null ? void 0 : l.path)
      ),
      alt: ""
    }
  }), {
    c() {
      e = N("div"), S(r.$$.fragment), Y(e, "class", "container svelte-wo3k18"), _(
        e,
        "table",
        /*type*/
        n[2] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        n[2] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        n[3]
      );
    },
    m(t, o) {
      F(t, e, o), G(r, e, null), s = !0;
    },
    p(t, [o]) {
      var i;
      const a = {};
      o & /*samples_dir, value*/
      3 && (a.src = /*samples_dir*/
      t[1] + /*value*/
      ((i = t[0]) == null ? void 0 : i.path)), r.$set(a), (!s || o & /*type*/
      4) && _(
        e,
        "table",
        /*type*/
        t[2] === "table"
      ), (!s || o & /*type*/
      4) && _(
        e,
        "gallery",
        /*type*/
        t[2] === "gallery"
      ), (!s || o & /*selected*/
      8) && _(
        e,
        "selected",
        /*selected*/
        t[3]
      );
    },
    i(t) {
      s || (I(r.$$.fragment, t), s = !0);
    },
    o(t) {
      V(r.$$.fragment, t), s = !1;
    },
    d(t) {
      t && x(e), j(r);
    }
  };
}
function A(n, e, r) {
  let { value: s } = e, { samples_dir: l } = e, { type: t } = e, { selected: o = !1 } = e;
  return n.$$set = (a) => {
    "value" in a && r(0, s = a.value), "samples_dir" in a && r(1, l = a.samples_dir), "type" in a && r(2, t = a.type), "selected" in a && r(3, o = a.selected);
  }, [s, l, t, o];
}
class J extends X {
  constructor(e) {
    super(), B(this, e, A, z, H, {
      value: 0,
      samples_dir: 1,
      type: 2,
      selected: 3
    });
  }
}
export {
  J as default
};
