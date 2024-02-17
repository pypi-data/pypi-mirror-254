const {
  SvelteComponent: gt,
  assign: ht,
  create_slot: wt,
  detach: pt,
  element: vt,
  get_all_dirty_from_scope: kt,
  get_slot_changes: yt,
  get_spread_update: Tt,
  init: zt,
  insert: qt,
  safe_not_equal: Ct,
  set_dynamic_element_data: Le,
  set_style: L,
  toggle_class: Z,
  transition_in: nt,
  transition_out: it,
  update_slot_base: Ft
} = window.__gradio__svelte__internal;
function Lt(n) {
  let e, t, l;
  const s = (
    /*#slots*/
    n[17].default
  ), i = wt(
    s,
    n,
    /*$$scope*/
    n[16],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-1t38q2d"
    }
  ], f = {};
  for (let a = 0; a < o.length; a += 1)
    f = ht(f, o[a]);
  return {
    c() {
      e = vt(
        /*tag*/
        n[14]
      ), i && i.c(), Le(
        /*tag*/
        n[14]
      )(e, f), Z(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), Z(
        e,
        "padded",
        /*padding*/
        n[6]
      ), Z(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), Z(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), L(e, "height", typeof /*height*/
      n[0] == "number" ? (
        /*height*/
        n[0] + "px"
      ) : void 0), L(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : void 0), L(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), L(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), L(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), L(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), L(e, "border-width", "var(--block-border-width)");
    },
    m(a, r) {
      qt(a, e, r), i && i.m(e, null), l = !0;
    },
    p(a, r) {
      i && i.p && (!l || r & /*$$scope*/
      65536) && Ft(
        i,
        s,
        a,
        /*$$scope*/
        a[16],
        l ? yt(
          s,
          /*$$scope*/
          a[16],
          r,
          null
        ) : kt(
          /*$$scope*/
          a[16]
        ),
        null
      ), Le(
        /*tag*/
        a[14]
      )(e, f = Tt(o, [
        (!l || r & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          a[7]
        ) },
        (!l || r & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          a[2]
        ) },
        (!l || r & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        a[3].join(" ") + " svelte-1t38q2d")) && { class: t }
      ])), Z(
        e,
        "hidden",
        /*visible*/
        a[10] === !1
      ), Z(
        e,
        "padded",
        /*padding*/
        a[6]
      ), Z(
        e,
        "border_focus",
        /*border_mode*/
        a[5] === "focus"
      ), Z(e, "hide-container", !/*explicit_call*/
      a[8] && !/*container*/
      a[9]), r & /*height*/
      1 && L(e, "height", typeof /*height*/
      a[0] == "number" ? (
        /*height*/
        a[0] + "px"
      ) : void 0), r & /*width*/
      2 && L(e, "width", typeof /*width*/
      a[1] == "number" ? `calc(min(${/*width*/
      a[1]}px, 100%))` : void 0), r & /*variant*/
      16 && L(
        e,
        "border-style",
        /*variant*/
        a[4]
      ), r & /*allow_overflow*/
      2048 && L(
        e,
        "overflow",
        /*allow_overflow*/
        a[11] ? "visible" : "hidden"
      ), r & /*scale*/
      4096 && L(
        e,
        "flex-grow",
        /*scale*/
        a[12]
      ), r & /*min_width*/
      8192 && L(e, "min-width", `calc(min(${/*min_width*/
      a[13]}px, 100%))`);
    },
    i(a) {
      l || (nt(i, a), l = !0);
    },
    o(a) {
      it(i, a), l = !1;
    },
    d(a) {
      a && pt(e), i && i.d(a);
    }
  };
}
function Et(n) {
  let e, t = (
    /*tag*/
    n[14] && Lt(n)
  );
  return {
    c() {
      t && t.c();
    },
    m(l, s) {
      t && t.m(l, s), e = !0;
    },
    p(l, [s]) {
      /*tag*/
      l[14] && t.p(l, s);
    },
    i(l) {
      e || (nt(t, l), e = !0);
    },
    o(l) {
      it(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function Bt(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e, { height: i = void 0 } = e, { width: o = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: a = [] } = e, { variant: r = "solid" } = e, { border_mode: _ = "base" } = e, { padding: u = !0 } = e, { type: b = "normal" } = e, { test_id: c = void 0 } = e, { explicit_call: d = !1 } = e, { container: y = !0 } = e, { visible: v = !0 } = e, { allow_overflow: F = !0 } = e, { scale: q = null } = e, { min_width: m = 0 } = e, z = b === "fieldset" ? "fieldset" : "div";
  return n.$$set = (h) => {
    "height" in h && t(0, i = h.height), "width" in h && t(1, o = h.width), "elem_id" in h && t(2, f = h.elem_id), "elem_classes" in h && t(3, a = h.elem_classes), "variant" in h && t(4, r = h.variant), "border_mode" in h && t(5, _ = h.border_mode), "padding" in h && t(6, u = h.padding), "type" in h && t(15, b = h.type), "test_id" in h && t(7, c = h.test_id), "explicit_call" in h && t(8, d = h.explicit_call), "container" in h && t(9, y = h.container), "visible" in h && t(10, v = h.visible), "allow_overflow" in h && t(11, F = h.allow_overflow), "scale" in h && t(12, q = h.scale), "min_width" in h && t(13, m = h.min_width), "$$scope" in h && t(16, s = h.$$scope);
  }, [
    i,
    o,
    f,
    a,
    r,
    _,
    u,
    c,
    d,
    y,
    v,
    F,
    q,
    m,
    z,
    b,
    s,
    l
  ];
}
class At extends gt {
  constructor(e) {
    super(), zt(this, e, Bt, Et, Ct, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 15,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Mt,
  attr: Nt,
  create_slot: St,
  detach: Vt,
  element: Xt,
  get_all_dirty_from_scope: It,
  get_slot_changes: Zt,
  init: Ot,
  insert: Pt,
  safe_not_equal: Rt,
  transition_in: jt,
  transition_out: Dt,
  update_slot_base: Ht
} = window.__gradio__svelte__internal;
function Ut(n) {
  let e, t;
  const l = (
    /*#slots*/
    n[1].default
  ), s = St(
    l,
    n,
    /*$$scope*/
    n[0],
    null
  );
  return {
    c() {
      e = Xt("div"), s && s.c(), Nt(e, "class", "svelte-1hnfib2");
    },
    m(i, o) {
      Pt(i, e, o), s && s.m(e, null), t = !0;
    },
    p(i, [o]) {
      s && s.p && (!t || o & /*$$scope*/
      1) && Ht(
        s,
        l,
        i,
        /*$$scope*/
        i[0],
        t ? Zt(
          l,
          /*$$scope*/
          i[0],
          o,
          null
        ) : It(
          /*$$scope*/
          i[0]
        ),
        null
      );
    },
    i(i) {
      t || (jt(s, i), t = !0);
    },
    o(i) {
      Dt(s, i), t = !1;
    },
    d(i) {
      i && Vt(e), s && s.d(i);
    }
  };
}
function Yt(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e;
  return n.$$set = (i) => {
    "$$scope" in i && t(0, s = i.$$scope);
  }, [s, l];
}
class Gt extends Mt {
  constructor(e) {
    super(), Ot(this, e, Yt, Ut, Rt, {});
  }
}
const {
  SvelteComponent: Kt,
  attr: Ee,
  check_outros: Jt,
  create_component: Qt,
  create_slot: Wt,
  destroy_component: xt,
  detach: ae,
  element: $t,
  empty: el,
  get_all_dirty_from_scope: tl,
  get_slot_changes: ll,
  group_outros: nl,
  init: il,
  insert: re,
  mount_component: sl,
  safe_not_equal: fl,
  set_data: ol,
  space: al,
  text: rl,
  toggle_class: U,
  transition_in: te,
  transition_out: _e,
  update_slot_base: _l
} = window.__gradio__svelte__internal;
function Be(n) {
  let e, t;
  return e = new Gt({
    props: {
      $$slots: { default: [ul] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Qt(e.$$.fragment);
    },
    m(l, s) {
      sl(e, l, s), t = !0;
    },
    p(l, s) {
      const i = {};
      s & /*$$scope, info*/
      10 && (i.$$scope = { dirty: s, ctx: l }), e.$set(i);
    },
    i(l) {
      t || (te(e.$$.fragment, l), t = !0);
    },
    o(l) {
      _e(e.$$.fragment, l), t = !1;
    },
    d(l) {
      xt(e, l);
    }
  };
}
function ul(n) {
  let e;
  return {
    c() {
      e = rl(
        /*info*/
        n[1]
      );
    },
    m(t, l) {
      re(t, e, l);
    },
    p(t, l) {
      l & /*info*/
      2 && ol(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && ae(e);
    }
  };
}
function cl(n) {
  let e, t, l, s;
  const i = (
    /*#slots*/
    n[2].default
  ), o = Wt(
    i,
    n,
    /*$$scope*/
    n[3],
    null
  );
  let f = (
    /*info*/
    n[1] && Be(n)
  );
  return {
    c() {
      e = $t("span"), o && o.c(), t = al(), f && f.c(), l = el(), Ee(e, "data-testid", "block-info"), Ee(e, "class", "svelte-22c38v"), U(e, "sr-only", !/*show_label*/
      n[0]), U(e, "hide", !/*show_label*/
      n[0]), U(
        e,
        "has-info",
        /*info*/
        n[1] != null
      );
    },
    m(a, r) {
      re(a, e, r), o && o.m(e, null), re(a, t, r), f && f.m(a, r), re(a, l, r), s = !0;
    },
    p(a, [r]) {
      o && o.p && (!s || r & /*$$scope*/
      8) && _l(
        o,
        i,
        a,
        /*$$scope*/
        a[3],
        s ? ll(
          i,
          /*$$scope*/
          a[3],
          r,
          null
        ) : tl(
          /*$$scope*/
          a[3]
        ),
        null
      ), (!s || r & /*show_label*/
      1) && U(e, "sr-only", !/*show_label*/
      a[0]), (!s || r & /*show_label*/
      1) && U(e, "hide", !/*show_label*/
      a[0]), (!s || r & /*info*/
      2) && U(
        e,
        "has-info",
        /*info*/
        a[1] != null
      ), /*info*/
      a[1] ? f ? (f.p(a, r), r & /*info*/
      2 && te(f, 1)) : (f = Be(a), f.c(), te(f, 1), f.m(l.parentNode, l)) : f && (nl(), _e(f, 1, 1, () => {
        f = null;
      }), Jt());
    },
    i(a) {
      s || (te(o, a), te(f), s = !0);
    },
    o(a) {
      _e(o, a), _e(f), s = !1;
    },
    d(a) {
      a && (ae(e), ae(t), ae(l)), o && o.d(a), f && f.d(a);
    }
  };
}
function dl(n, e, t) {
  let { $$slots: l = {}, $$scope: s } = e, { show_label: i = !0 } = e, { info: o = void 0 } = e;
  return n.$$set = (f) => {
    "show_label" in f && t(0, i = f.show_label), "info" in f && t(1, o = f.info), "$$scope" in f && t(3, s = f.$$scope);
  }, [i, o, l, s];
}
class ml extends Kt {
  constructor(e) {
    super(), il(this, e, dl, cl, fl, { show_label: 0, info: 1 });
  }
}
const bl = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], Ae = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
bl.reduce(
  (n, { color: e, primary: t, secondary: l }) => ({
    ...n,
    [e]: {
      primary: Ae[e][t],
      secondary: Ae[e][l]
    }
  }),
  {}
);
function G(n) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; n > 1e3 && t < e.length - 1; )
    n /= 1e3, t++;
  let l = e[t];
  return (Number.isInteger(n) ? n : n.toFixed(1)) + l;
}
function ue() {
}
function gl(n, e) {
  return n != n ? e == e : n !== e || n && typeof n == "object" || typeof n == "function";
}
const st = typeof window < "u";
let Me = st ? () => window.performance.now() : () => Date.now(), ft = st ? (n) => requestAnimationFrame(n) : ue;
const J = /* @__PURE__ */ new Set();
function ot(n) {
  J.forEach((e) => {
    e.c(n) || (J.delete(e), e.f());
  }), J.size !== 0 && ft(ot);
}
function hl(n) {
  let e;
  return J.size === 0 && ft(ot), {
    promise: new Promise((t) => {
      J.add(e = { c: n, f: t });
    }),
    abort() {
      J.delete(e);
    }
  };
}
const Y = [];
function wl(n, e = ue) {
  let t;
  const l = /* @__PURE__ */ new Set();
  function s(f) {
    if (gl(n, f) && (n = f, t)) {
      const a = !Y.length;
      for (const r of l)
        r[1](), Y.push(r, n);
      if (a) {
        for (let r = 0; r < Y.length; r += 2)
          Y[r][0](Y[r + 1]);
        Y.length = 0;
      }
    }
  }
  function i(f) {
    s(f(n));
  }
  function o(f, a = ue) {
    const r = [f, a];
    return l.add(r), l.size === 1 && (t = e(s, i) || ue), f(n), () => {
      l.delete(r), l.size === 0 && t && (t(), t = null);
    };
  }
  return { set: s, update: i, subscribe: o };
}
function Ne(n) {
  return Object.prototype.toString.call(n) === "[object Date]";
}
function we(n, e, t, l) {
  if (typeof t == "number" || Ne(t)) {
    const s = l - t, i = (t - e) / (n.dt || 1 / 60), o = n.opts.stiffness * s, f = n.opts.damping * i, a = (o - f) * n.inv_mass, r = (i + a) * n.dt;
    return Math.abs(r) < n.opts.precision && Math.abs(s) < n.opts.precision ? l : (n.settled = !1, Ne(t) ? new Date(t.getTime() + r) : t + r);
  } else {
    if (Array.isArray(t))
      return t.map(
        (s, i) => we(n, e[i], t[i], l[i])
      );
    if (typeof t == "object") {
      const s = {};
      for (const i in t)
        s[i] = we(n, e[i], t[i], l[i]);
      return s;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Se(n, e = {}) {
  const t = wl(n), { stiffness: l = 0.15, damping: s = 0.8, precision: i = 0.01 } = e;
  let o, f, a, r = n, _ = n, u = 1, b = 0, c = !1;
  function d(v, F = {}) {
    _ = v;
    const q = a = {};
    return n == null || F.hard || y.stiffness >= 1 && y.damping >= 1 ? (c = !0, o = Me(), r = v, t.set(n = _), Promise.resolve()) : (F.soft && (b = 1 / ((F.soft === !0 ? 0.5 : +F.soft) * 60), u = 0), f || (o = Me(), c = !1, f = hl((m) => {
      if (c)
        return c = !1, f = null, !1;
      u = Math.min(u + b, 1);
      const z = {
        inv_mass: u,
        opts: y,
        settled: !0,
        dt: (m - o) * 60 / 1e3
      }, h = we(z, r, n, _);
      return o = m, r = n, t.set(n = h), z.settled && (f = null), !z.settled;
    })), new Promise((m) => {
      f.promise.then(() => {
        q === a && m();
      });
    }));
  }
  const y = {
    set: d,
    update: (v, F) => d(v(_, n), F),
    subscribe: t.subscribe,
    stiffness: l,
    damping: s,
    precision: i
  };
  return y;
}
const {
  SvelteComponent: pl,
  append: M,
  attr: T,
  component_subscribe: Ve,
  detach: vl,
  element: kl,
  init: yl,
  insert: Tl,
  noop: Xe,
  safe_not_equal: zl,
  set_style: fe,
  svg_element: N,
  toggle_class: Ie
} = window.__gradio__svelte__internal, { onMount: ql } = window.__gradio__svelte__internal;
function Cl(n) {
  let e, t, l, s, i, o, f, a, r, _, u, b;
  return {
    c() {
      e = kl("div"), t = N("svg"), l = N("g"), s = N("path"), i = N("path"), o = N("path"), f = N("path"), a = N("g"), r = N("path"), _ = N("path"), u = N("path"), b = N("path"), T(s, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), T(s, "fill", "#FF7C00"), T(s, "fill-opacity", "0.4"), T(s, "class", "svelte-43sxxs"), T(i, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), T(i, "fill", "#FF7C00"), T(i, "class", "svelte-43sxxs"), T(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), T(o, "fill", "#FF7C00"), T(o, "fill-opacity", "0.4"), T(o, "class", "svelte-43sxxs"), T(f, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), T(f, "fill", "#FF7C00"), T(f, "class", "svelte-43sxxs"), fe(l, "transform", "translate(" + /*$top*/
      n[1][0] + "px, " + /*$top*/
      n[1][1] + "px)"), T(r, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), T(r, "fill", "#FF7C00"), T(r, "fill-opacity", "0.4"), T(r, "class", "svelte-43sxxs"), T(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), T(_, "fill", "#FF7C00"), T(_, "class", "svelte-43sxxs"), T(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), T(u, "fill", "#FF7C00"), T(u, "fill-opacity", "0.4"), T(u, "class", "svelte-43sxxs"), T(b, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), T(b, "fill", "#FF7C00"), T(b, "class", "svelte-43sxxs"), fe(a, "transform", "translate(" + /*$bottom*/
      n[2][0] + "px, " + /*$bottom*/
      n[2][1] + "px)"), T(t, "viewBox", "-1200 -1200 3000 3000"), T(t, "fill", "none"), T(t, "xmlns", "http://www.w3.org/2000/svg"), T(t, "class", "svelte-43sxxs"), T(e, "class", "svelte-43sxxs"), Ie(
        e,
        "margin",
        /*margin*/
        n[0]
      );
    },
    m(c, d) {
      Tl(c, e, d), M(e, t), M(t, l), M(l, s), M(l, i), M(l, o), M(l, f), M(t, a), M(a, r), M(a, _), M(a, u), M(a, b);
    },
    p(c, [d]) {
      d & /*$top*/
      2 && fe(l, "transform", "translate(" + /*$top*/
      c[1][0] + "px, " + /*$top*/
      c[1][1] + "px)"), d & /*$bottom*/
      4 && fe(a, "transform", "translate(" + /*$bottom*/
      c[2][0] + "px, " + /*$bottom*/
      c[2][1] + "px)"), d & /*margin*/
      1 && Ie(
        e,
        "margin",
        /*margin*/
        c[0]
      );
    },
    i: Xe,
    o: Xe,
    d(c) {
      c && vl(e);
    }
  };
}
function Fl(n, e, t) {
  let l, s, { margin: i = !0 } = e;
  const o = Se([0, 0]);
  Ve(n, o, (b) => t(1, l = b));
  const f = Se([0, 0]);
  Ve(n, f, (b) => t(2, s = b));
  let a;
  async function r() {
    await Promise.all([o.set([125, 140]), f.set([-125, -140])]), await Promise.all([o.set([-125, 140]), f.set([125, -140])]), await Promise.all([o.set([-125, 0]), f.set([125, -0])]), await Promise.all([o.set([125, 0]), f.set([-125, 0])]);
  }
  async function _() {
    await r(), a || _();
  }
  async function u() {
    await Promise.all([o.set([125, 0]), f.set([-125, 0])]), _();
  }
  return ql(() => (u(), () => a = !0)), n.$$set = (b) => {
    "margin" in b && t(0, i = b.margin);
  }, [i, l, s, o, f];
}
class Ll extends pl {
  constructor(e) {
    super(), yl(this, e, Fl, Cl, zl, { margin: 0 });
  }
}
const {
  SvelteComponent: El,
  append: H,
  attr: S,
  binding_callbacks: Ze,
  check_outros: at,
  create_component: Bl,
  create_slot: Al,
  destroy_component: Ml,
  destroy_each: rt,
  detach: w,
  element: X,
  empty: x,
  ensure_array_like: ce,
  get_all_dirty_from_scope: Nl,
  get_slot_changes: Sl,
  group_outros: _t,
  init: Vl,
  insert: p,
  mount_component: Xl,
  noop: pe,
  safe_not_equal: Il,
  set_data: A,
  set_style: P,
  space: V,
  text: C,
  toggle_class: B,
  transition_in: Q,
  transition_out: W,
  update_slot_base: Zl
} = window.__gradio__svelte__internal, { tick: Ol } = window.__gradio__svelte__internal, { onDestroy: Pl } = window.__gradio__svelte__internal, Rl = (n) => ({}), Oe = (n) => ({});
function Pe(n, e, t) {
  const l = n.slice();
  return l[38] = e[t], l[40] = t, l;
}
function Re(n, e, t) {
  const l = n.slice();
  return l[38] = e[t], l;
}
function jl(n) {
  let e, t = (
    /*i18n*/
    n[1]("common.error") + ""
  ), l, s, i;
  const o = (
    /*#slots*/
    n[29].error
  ), f = Al(
    o,
    n,
    /*$$scope*/
    n[28],
    Oe
  );
  return {
    c() {
      e = X("span"), l = C(t), s = V(), f && f.c(), S(e, "class", "error svelte-14miwb5");
    },
    m(a, r) {
      p(a, e, r), H(e, l), p(a, s, r), f && f.m(a, r), i = !0;
    },
    p(a, r) {
      (!i || r[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      a[1]("common.error") + "") && A(l, t), f && f.p && (!i || r[0] & /*$$scope*/
      268435456) && Zl(
        f,
        o,
        a,
        /*$$scope*/
        a[28],
        i ? Sl(
          o,
          /*$$scope*/
          a[28],
          r,
          Rl
        ) : Nl(
          /*$$scope*/
          a[28]
        ),
        Oe
      );
    },
    i(a) {
      i || (Q(f, a), i = !0);
    },
    o(a) {
      W(f, a), i = !1;
    },
    d(a) {
      a && (w(e), w(s)), f && f.d(a);
    }
  };
}
function Dl(n) {
  let e, t, l, s, i, o, f, a, r, _ = (
    /*variant*/
    n[8] === "default" && /*show_eta_bar*/
    n[18] && /*show_progress*/
    n[6] === "full" && je(n)
  );
  function u(m, z) {
    if (
      /*progress*/
      m[7]
    )
      return Yl;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return Ul;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return Hl;
  }
  let b = u(n), c = b && b(n), d = (
    /*timer*/
    n[5] && Ue(n)
  );
  const y = [Ql, Jl], v = [];
  function F(m, z) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(i = F(n)) && (o = v[i] = y[i](n));
  let q = !/*timer*/
  n[5] && xe(n);
  return {
    c() {
      _ && _.c(), e = V(), t = X("div"), c && c.c(), l = V(), d && d.c(), s = V(), o && o.c(), f = V(), q && q.c(), a = x(), S(t, "class", "progress-text svelte-14miwb5"), B(
        t,
        "meta-text-center",
        /*variant*/
        n[8] === "center"
      ), B(
        t,
        "meta-text",
        /*variant*/
        n[8] === "default"
      );
    },
    m(m, z) {
      _ && _.m(m, z), p(m, e, z), p(m, t, z), c && c.m(t, null), H(t, l), d && d.m(t, null), p(m, s, z), ~i && v[i].m(m, z), p(m, f, z), q && q.m(m, z), p(m, a, z), r = !0;
    },
    p(m, z) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? _ ? _.p(m, z) : (_ = je(m), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), b === (b = u(m)) && c ? c.p(m, z) : (c && c.d(1), c = b && b(m), c && (c.c(), c.m(t, l))), /*timer*/
      m[5] ? d ? d.p(m, z) : (d = Ue(m), d.c(), d.m(t, null)) : d && (d.d(1), d = null), (!r || z[0] & /*variant*/
      256) && B(
        t,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!r || z[0] & /*variant*/
      256) && B(
        t,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let h = i;
      i = F(m), i === h ? ~i && v[i].p(m, z) : (o && (_t(), W(v[h], 1, 1, () => {
        v[h] = null;
      }), at()), ~i ? (o = v[i], o ? o.p(m, z) : (o = v[i] = y[i](m), o.c()), Q(o, 1), o.m(f.parentNode, f)) : o = null), /*timer*/
      m[5] ? q && (q.d(1), q = null) : q ? q.p(m, z) : (q = xe(m), q.c(), q.m(a.parentNode, a));
    },
    i(m) {
      r || (Q(o), r = !0);
    },
    o(m) {
      W(o), r = !1;
    },
    d(m) {
      m && (w(e), w(t), w(s), w(f), w(a)), _ && _.d(m), c && c.d(), d && d.d(), ~i && v[i].d(m), q && q.d(m);
    }
  };
}
function je(n) {
  let e, t = `translateX(${/*eta_level*/
  (n[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = X("div"), S(e, "class", "eta-bar svelte-14miwb5"), P(e, "transform", t);
    },
    m(l, s) {
      p(l, e, s);
    },
    p(l, s) {
      s[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (l[17] || 0) * 100 - 100}%)`) && P(e, "transform", t);
    },
    d(l) {
      l && w(e);
    }
  };
}
function Hl(n) {
  let e;
  return {
    c() {
      e = C("processing |");
    },
    m(t, l) {
      p(t, e, l);
    },
    p: pe,
    d(t) {
      t && w(e);
    }
  };
}
function Ul(n) {
  let e, t = (
    /*queue_position*/
    n[2] + 1 + ""
  ), l, s, i, o;
  return {
    c() {
      e = C("queue: "), l = C(t), s = C("/"), i = C(
        /*queue_size*/
        n[3]
      ), o = C(" |");
    },
    m(f, a) {
      p(f, e, a), p(f, l, a), p(f, s, a), p(f, i, a), p(f, o, a);
    },
    p(f, a) {
      a[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      f[2] + 1 + "") && A(l, t), a[0] & /*queue_size*/
      8 && A(
        i,
        /*queue_size*/
        f[3]
      );
    },
    d(f) {
      f && (w(e), w(l), w(s), w(i), w(o));
    }
  };
}
function Yl(n) {
  let e, t = ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let s = 0; s < t.length; s += 1)
    l[s] = He(Re(n, t, s));
  return {
    c() {
      for (let s = 0; s < l.length; s += 1)
        l[s].c();
      e = x();
    },
    m(s, i) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(s, i);
      p(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress*/
      128) {
        t = ce(
          /*progress*/
          s[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const f = Re(s, t, o);
          l[o] ? l[o].p(f, i) : (l[o] = He(f), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(s) {
      s && w(e), rt(l, s);
    }
  };
}
function De(n) {
  let e, t = (
    /*p*/
    n[38].unit + ""
  ), l, s, i = " ", o;
  function f(_, u) {
    return (
      /*p*/
      _[38].length != null ? Kl : Gl
    );
  }
  let a = f(n), r = a(n);
  return {
    c() {
      r.c(), e = V(), l = C(t), s = C(" | "), o = C(i);
    },
    m(_, u) {
      r.m(_, u), p(_, e, u), p(_, l, u), p(_, s, u), p(_, o, u);
    },
    p(_, u) {
      a === (a = f(_)) && r ? r.p(_, u) : (r.d(1), r = a(_), r && (r.c(), r.m(e.parentNode, e))), u[0] & /*progress*/
      128 && t !== (t = /*p*/
      _[38].unit + "") && A(l, t);
    },
    d(_) {
      _ && (w(e), w(l), w(s), w(o)), r.d(_);
    }
  };
}
function Gl(n) {
  let e = G(
    /*p*/
    n[38].index || 0
  ) + "", t;
  return {
    c() {
      t = C(e);
    },
    m(l, s) {
      p(l, t, s);
    },
    p(l, s) {
      s[0] & /*progress*/
      128 && e !== (e = G(
        /*p*/
        l[38].index || 0
      ) + "") && A(t, e);
    },
    d(l) {
      l && w(t);
    }
  };
}
function Kl(n) {
  let e = G(
    /*p*/
    n[38].index || 0
  ) + "", t, l, s = G(
    /*p*/
    n[38].length
  ) + "", i;
  return {
    c() {
      t = C(e), l = C("/"), i = C(s);
    },
    m(o, f) {
      p(o, t, f), p(o, l, f), p(o, i, f);
    },
    p(o, f) {
      f[0] & /*progress*/
      128 && e !== (e = G(
        /*p*/
        o[38].index || 0
      ) + "") && A(t, e), f[0] & /*progress*/
      128 && s !== (s = G(
        /*p*/
        o[38].length
      ) + "") && A(i, s);
    },
    d(o) {
      o && (w(t), w(l), w(i));
    }
  };
}
function He(n) {
  let e, t = (
    /*p*/
    n[38].index != null && De(n)
  );
  return {
    c() {
      t && t.c(), e = x();
    },
    m(l, s) {
      t && t.m(l, s), p(l, e, s);
    },
    p(l, s) {
      /*p*/
      l[38].index != null ? t ? t.p(l, s) : (t = De(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && w(e), t && t.d(l);
    }
  };
}
function Ue(n) {
  let e, t = (
    /*eta*/
    n[0] ? `/${/*formatted_eta*/
    n[19]}` : ""
  ), l, s;
  return {
    c() {
      e = C(
        /*formatted_timer*/
        n[20]
      ), l = C(t), s = C("s");
    },
    m(i, o) {
      p(i, e, o), p(i, l, o), p(i, s, o);
    },
    p(i, o) {
      o[0] & /*formatted_timer*/
      1048576 && A(
        e,
        /*formatted_timer*/
        i[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      i[0] ? `/${/*formatted_eta*/
      i[19]}` : "") && A(l, t);
    },
    d(i) {
      i && (w(e), w(l), w(s));
    }
  };
}
function Jl(n) {
  let e, t;
  return e = new Ll({
    props: { margin: (
      /*variant*/
      n[8] === "default"
    ) }
  }), {
    c() {
      Bl(e.$$.fragment);
    },
    m(l, s) {
      Xl(e, l, s), t = !0;
    },
    p(l, s) {
      const i = {};
      s[0] & /*variant*/
      256 && (i.margin = /*variant*/
      l[8] === "default"), e.$set(i);
    },
    i(l) {
      t || (Q(e.$$.fragment, l), t = !0);
    },
    o(l) {
      W(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Ml(e, l);
    }
  };
}
function Ql(n) {
  let e, t, l, s, i, o = `${/*last_progress_level*/
  n[15] * 100}%`, f = (
    /*progress*/
    n[7] != null && Ye(n)
  );
  return {
    c() {
      e = X("div"), t = X("div"), f && f.c(), l = V(), s = X("div"), i = X("div"), S(t, "class", "progress-level-inner svelte-14miwb5"), S(i, "class", "progress-bar svelte-14miwb5"), P(i, "width", o), S(s, "class", "progress-bar-wrap svelte-14miwb5"), S(e, "class", "progress-level svelte-14miwb5");
    },
    m(a, r) {
      p(a, e, r), H(e, t), f && f.m(t, null), H(e, l), H(e, s), H(s, i), n[30](i);
    },
    p(a, r) {
      /*progress*/
      a[7] != null ? f ? f.p(a, r) : (f = Ye(a), f.c(), f.m(t, null)) : f && (f.d(1), f = null), r[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      a[15] * 100}%`) && P(i, "width", o);
    },
    i: pe,
    o: pe,
    d(a) {
      a && w(e), f && f.d(), n[30](null);
    }
  };
}
function Ye(n) {
  let e, t = ce(
    /*progress*/
    n[7]
  ), l = [];
  for (let s = 0; s < t.length; s += 1)
    l[s] = We(Pe(n, t, s));
  return {
    c() {
      for (let s = 0; s < l.length; s += 1)
        l[s].c();
      e = x();
    },
    m(s, i) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(s, i);
      p(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress_level, progress*/
      16512) {
        t = ce(
          /*progress*/
          s[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const f = Pe(s, t, o);
          l[o] ? l[o].p(f, i) : (l[o] = We(f), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(s) {
      s && w(e), rt(l, s);
    }
  };
}
function Ge(n) {
  let e, t, l, s, i = (
    /*i*/
    n[40] !== 0 && Wl()
  ), o = (
    /*p*/
    n[38].desc != null && Ke(n)
  ), f = (
    /*p*/
    n[38].desc != null && /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[40]
    ] != null && Je()
  ), a = (
    /*progress_level*/
    n[14] != null && Qe(n)
  );
  return {
    c() {
      i && i.c(), e = V(), o && o.c(), t = V(), f && f.c(), l = V(), a && a.c(), s = x();
    },
    m(r, _) {
      i && i.m(r, _), p(r, e, _), o && o.m(r, _), p(r, t, _), f && f.m(r, _), p(r, l, _), a && a.m(r, _), p(r, s, _);
    },
    p(r, _) {
      /*p*/
      r[38].desc != null ? o ? o.p(r, _) : (o = Ke(r), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      r[38].desc != null && /*progress_level*/
      r[14] && /*progress_level*/
      r[14][
        /*i*/
        r[40]
      ] != null ? f || (f = Je(), f.c(), f.m(l.parentNode, l)) : f && (f.d(1), f = null), /*progress_level*/
      r[14] != null ? a ? a.p(r, _) : (a = Qe(r), a.c(), a.m(s.parentNode, s)) : a && (a.d(1), a = null);
    },
    d(r) {
      r && (w(e), w(t), w(l), w(s)), i && i.d(r), o && o.d(r), f && f.d(r), a && a.d(r);
    }
  };
}
function Wl(n) {
  let e;
  return {
    c() {
      e = C(" /");
    },
    m(t, l) {
      p(t, e, l);
    },
    d(t) {
      t && w(e);
    }
  };
}
function Ke(n) {
  let e = (
    /*p*/
    n[38].desc + ""
  ), t;
  return {
    c() {
      t = C(e);
    },
    m(l, s) {
      p(l, t, s);
    },
    p(l, s) {
      s[0] & /*progress*/
      128 && e !== (e = /*p*/
      l[38].desc + "") && A(t, e);
    },
    d(l) {
      l && w(t);
    }
  };
}
function Je(n) {
  let e;
  return {
    c() {
      e = C("-");
    },
    m(t, l) {
      p(t, e, l);
    },
    d(t) {
      t && w(e);
    }
  };
}
function Qe(n) {
  let e = (100 * /*progress_level*/
  (n[14][
    /*i*/
    n[40]
  ] || 0)).toFixed(1) + "", t, l;
  return {
    c() {
      t = C(e), l = C("%");
    },
    m(s, i) {
      p(s, t, i), p(s, l, i);
    },
    p(s, i) {
      i[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (s[14][
        /*i*/
        s[40]
      ] || 0)).toFixed(1) + "") && A(t, e);
    },
    d(s) {
      s && (w(t), w(l));
    }
  };
}
function We(n) {
  let e, t = (
    /*p*/
    (n[38].desc != null || /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[40]
    ] != null) && Ge(n)
  );
  return {
    c() {
      t && t.c(), e = x();
    },
    m(l, s) {
      t && t.m(l, s), p(l, e, s);
    },
    p(l, s) {
      /*p*/
      l[38].desc != null || /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[40]
      ] != null ? t ? t.p(l, s) : (t = Ge(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && w(e), t && t.d(l);
    }
  };
}
function xe(n) {
  let e, t;
  return {
    c() {
      e = X("p"), t = C(
        /*loading_text*/
        n[9]
      ), S(e, "class", "loading svelte-14miwb5");
    },
    m(l, s) {
      p(l, e, s), H(e, t);
    },
    p(l, s) {
      s[0] & /*loading_text*/
      512 && A(
        t,
        /*loading_text*/
        l[9]
      );
    },
    d(l) {
      l && w(e);
    }
  };
}
function xl(n) {
  let e, t, l, s, i;
  const o = [Dl, jl], f = [];
  function a(r, _) {
    return (
      /*status*/
      r[4] === "pending" ? 0 : (
        /*status*/
        r[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = a(n)) && (l = f[t] = o[t](n)), {
    c() {
      e = X("div"), l && l.c(), S(e, "class", s = "wrap " + /*variant*/
      n[8] + " " + /*show_progress*/
      n[6] + " svelte-14miwb5"), B(e, "hide", !/*status*/
      n[4] || /*status*/
      n[4] === "complete" || /*show_progress*/
      n[6] === "hidden"), B(
        e,
        "translucent",
        /*variant*/
        n[8] === "center" && /*status*/
        (n[4] === "pending" || /*status*/
        n[4] === "error") || /*translucent*/
        n[11] || /*show_progress*/
        n[6] === "minimal"
      ), B(
        e,
        "generating",
        /*status*/
        n[4] === "generating"
      ), B(
        e,
        "border",
        /*border*/
        n[12]
      ), P(
        e,
        "position",
        /*absolute*/
        n[10] ? "absolute" : "static"
      ), P(
        e,
        "padding",
        /*absolute*/
        n[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(r, _) {
      p(r, e, _), ~t && f[t].m(e, null), n[31](e), i = !0;
    },
    p(r, _) {
      let u = t;
      t = a(r), t === u ? ~t && f[t].p(r, _) : (l && (_t(), W(f[u], 1, 1, () => {
        f[u] = null;
      }), at()), ~t ? (l = f[t], l ? l.p(r, _) : (l = f[t] = o[t](r), l.c()), Q(l, 1), l.m(e, null)) : l = null), (!i || _[0] & /*variant, show_progress*/
      320 && s !== (s = "wrap " + /*variant*/
      r[8] + " " + /*show_progress*/
      r[6] + " svelte-14miwb5")) && S(e, "class", s), (!i || _[0] & /*variant, show_progress, status, show_progress*/
      336) && B(e, "hide", !/*status*/
      r[4] || /*status*/
      r[4] === "complete" || /*show_progress*/
      r[6] === "hidden"), (!i || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && B(
        e,
        "translucent",
        /*variant*/
        r[8] === "center" && /*status*/
        (r[4] === "pending" || /*status*/
        r[4] === "error") || /*translucent*/
        r[11] || /*show_progress*/
        r[6] === "minimal"
      ), (!i || _[0] & /*variant, show_progress, status*/
      336) && B(
        e,
        "generating",
        /*status*/
        r[4] === "generating"
      ), (!i || _[0] & /*variant, show_progress, border*/
      4416) && B(
        e,
        "border",
        /*border*/
        r[12]
      ), _[0] & /*absolute*/
      1024 && P(
        e,
        "position",
        /*absolute*/
        r[10] ? "absolute" : "static"
      ), _[0] & /*absolute*/
      1024 && P(
        e,
        "padding",
        /*absolute*/
        r[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(r) {
      i || (Q(l), i = !0);
    },
    o(r) {
      W(l), i = !1;
    },
    d(r) {
      r && w(e), ~t && f[t].d(), n[31](null);
    }
  };
}
let oe = [], me = !1;
async function $l(n, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (oe.push(n), !me)
      me = !0;
    else
      return;
    await Ol(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let l = 0; l < oe.length; l++) {
        const i = oe[l].getBoundingClientRect();
        (l === 0 || i.top + window.scrollY <= t[0]) && (t[0] = i.top + window.scrollY, t[1] = l);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), me = !1, oe = [];
    });
  }
}
function en(n, e, t) {
  let l, { $$slots: s = {}, $$scope: i } = e, { i18n: o } = e, { eta: f = null } = e, { queue: a = !1 } = e, { queue_position: r } = e, { queue_size: _ } = e, { status: u } = e, { scroll_to_output: b = !1 } = e, { timer: c = !0 } = e, { show_progress: d = "full" } = e, { message: y = null } = e, { progress: v = null } = e, { variant: F = "default" } = e, { loading_text: q = "Loading..." } = e, { absolute: m = !0 } = e, { translucent: z = !1 } = e, { border: h = !1 } = e, { autoscroll: $ } = e, R, k = !1, se = 0, j = 0, de = null, Te = 0, D = null, ee, I = null, ze = !0;
  const dt = () => {
    t(25, se = performance.now()), t(26, j = 0), k = !0, qe();
  };
  function qe() {
    requestAnimationFrame(() => {
      t(26, j = (performance.now() - se) / 1e3), k && qe();
    });
  }
  function Ce() {
    t(26, j = 0), k && (k = !1);
  }
  Pl(() => {
    k && Ce();
  });
  let Fe = null;
  function mt(g) {
    Ze[g ? "unshift" : "push"](() => {
      I = g, t(16, I), t(7, v), t(14, D), t(15, ee);
    });
  }
  function bt(g) {
    Ze[g ? "unshift" : "push"](() => {
      R = g, t(13, R);
    });
  }
  return n.$$set = (g) => {
    "i18n" in g && t(1, o = g.i18n), "eta" in g && t(0, f = g.eta), "queue" in g && t(21, a = g.queue), "queue_position" in g && t(2, r = g.queue_position), "queue_size" in g && t(3, _ = g.queue_size), "status" in g && t(4, u = g.status), "scroll_to_output" in g && t(22, b = g.scroll_to_output), "timer" in g && t(5, c = g.timer), "show_progress" in g && t(6, d = g.show_progress), "message" in g && t(23, y = g.message), "progress" in g && t(7, v = g.progress), "variant" in g && t(8, F = g.variant), "loading_text" in g && t(9, q = g.loading_text), "absolute" in g && t(10, m = g.absolute), "translucent" in g && t(11, z = g.translucent), "border" in g && t(12, h = g.border), "autoscroll" in g && t(24, $ = g.autoscroll), "$$scope" in g && t(28, i = g.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (f === null ? t(0, f = de) : a && t(0, f = (performance.now() - se) / 1e3 + f), f != null && (t(19, Fe = f.toFixed(1)), t(27, de = f))), n.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && t(17, Te = f === null || f <= 0 || !j ? null : Math.min(j / f, 1)), n.$$.dirty[0] & /*progress*/
    128 && v != null && t(18, ze = !1), n.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? t(14, D = v.map((g) => {
      if (g.index != null && g.length != null)
        return g.index / g.length;
      if (g.progress != null)
        return g.progress;
    })) : t(14, D = null), D ? (t(15, ee = D[D.length - 1]), I && (ee === 0 ? t(16, I.style.transition = "0", I) : t(16, I.style.transition = "150ms", I))) : t(15, ee = void 0)), n.$$.dirty[0] & /*status*/
    16 && (u === "pending" ? dt() : Ce()), n.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && R && b && (u === "pending" || u === "complete") && $l(R, $), n.$$.dirty[0] & /*status, message*/
    8388624, n.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, l = j.toFixed(1));
  }, [
    f,
    o,
    r,
    _,
    u,
    c,
    d,
    v,
    F,
    q,
    m,
    z,
    h,
    R,
    D,
    ee,
    I,
    Te,
    ze,
    Fe,
    l,
    a,
    b,
    y,
    $,
    se,
    j,
    de,
    i,
    s,
    mt,
    bt
  ];
}
class tn extends El {
  constructor(e) {
    super(), Vl(
      this,
      e,
      en,
      xl,
      Il,
      {
        i18n: 1,
        eta: 0,
        queue: 21,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
var ln = function() {
  var n = this, e = /{[A-Z_]+[0-9]*}/ig, t = {
    URL: "((?:(?:[a-z][a-z\\d+\\-.]*:\\/{2}(?:(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})+|[0-9.]+|\\[[a-z0-9.]+:[a-z0-9.]+:[a-z0-9.:]+\\])(?::\\d*)?(?:\\/(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})*)*(?:\\?(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?(?:#(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?)|(?:www\\.(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})+(?::\\d*)?(?:\\/(?:[a-z0-9\\-._~\\!$&'*+,;=:@|]+|%[\\dA-F]{2})*)*(?:\\?(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?(?:#(?:[a-z0-9\\-._~\\!$&'*+,;=:@\\/?|]+|%[\\dA-F]{2})*)?)))",
    LINK: `([a-z0-9-./]+[^"' ]*)`,
    EMAIL: "((?:[\\w!#$%&'*+-/=?^`{|}~]+.)*(?:[\\w!#$%'*+-/=?^`{|}~]|&)+@(?:(?:(?:(?:(?:[a-z0-9]{1}[a-z0-9-]{0,62}[a-z0-9]{1})|[a-z]).)+[a-z]{2,6})|(?:\\d{1,3}.){3}\\d{1,3}(?::\\d{1,5})?))",
    TEXT: "(.*?)",
    SIMPLETEXT: "([a-zA-Z0-9-+.,_ ]+)",
    INTTEXT: "([a-zA-Z0-9-+,_. ]+)",
    IDENTIFIER: "([a-zA-Z0-9-_]+)",
    COLOR: "([a-z]+|#[0-9abcdef]+)",
    NUMBER: "([0-9]+)"
  }, l = [], s = [], i = [], o = [], f = function(_) {
    var u = _.match(e), b = u.length, c = 0, d = "";
    if (b <= 0)
      return new RegExp(r(_), "g");
    for (; c < b; c += 1) {
      var y = u[c].replace(/[{}0-9]/g, "");
      t[y] && (d += r(_.substr(0, _.indexOf(u[c]))) + t[y], _ = _.substr(_.indexOf(u[c]) + u[c].length));
    }
    return d += r(_), new RegExp(d, "gi");
  }, a = function(_) {
    var u = _.match(e), b = u.length, c = 0, d = "", y = {}, v = 0;
    if (b <= 0)
      return _;
    for (; c < b; c += 1) {
      var F = u[c].replace(/[{}0-9]/g, ""), q;
      y[u[c]] ? q = y[u[c]] : (v += 1, q = v, y[u[c]] = q), t[F] && (d += _.substr(0, _.indexOf(u[c])) + "$" + q, _ = _.substr(_.indexOf(u[c]) + u[c].length));
    }
    return d += _, d;
  };
  n.addBBCode = function(_, u) {
    l.push(f(_)), s.push(a(u)), i.push(f(u)), o.push(a(_));
  }, n.bbcodeToHtml = function(_) {
    for (var u = l.length, b = 0; b < u; b += 1)
      _ = _.replace(l[b], s[b]);
    return _;
  }, n.htmlToBBCode = function(_) {
    for (var u = i.length, b = 0; b < u; b += 1)
      _ = _.replace(i[b], o[b]);
    return _;
  };
  function r(_, u) {
    return (_ + "").replace(new RegExp("[.\\\\+*?\\[\\^\\]$(){}=!<>|:\\" + (u || "") + "-]", "g"), "\\$&");
  }
  n.addBBCode("[b]{TEXT}[/b]", "<strong>{TEXT}</strong>"), n.addBBCode("[i]{TEXT}[/i]", "<em>{TEXT}</em>"), n.addBBCode("[u]{TEXT}[/u]", '<span style="text-decoration:underline;">{TEXT}</span>'), n.addBBCode("[s]{TEXT}[/s]", '<span style="text-decoration:line-through;">{TEXT}</span>'), n.addBBCode("[color={COLOR}]{TEXT}[/color]", '<span style="color:{COLOR}">{TEXT}</span>');
}, nn = new ln();
const {
  HtmlTag: sn,
  SvelteComponent: fn,
  append: $e,
  assign: on,
  attr: O,
  binding_callbacks: an,
  check_outros: rn,
  create_component: ve,
  destroy_component: ke,
  detach: ne,
  element: et,
  empty: _n,
  flush: E,
  get_spread_object: un,
  get_spread_update: cn,
  group_outros: dn,
  init: mn,
  insert: ie,
  listen: be,
  mount_component: ye,
  run_all: bn,
  safe_not_equal: gn,
  set_data: ut,
  space: tt,
  text: ct,
  toggle_class: ge,
  transition_in: K,
  transition_out: le
} = window.__gradio__svelte__internal, { tick: he } = window.__gradio__svelte__internal;
function lt(n) {
  let e, t;
  const l = [
    { autoscroll: (
      /*gradio*/
      n[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      n[1].i18n
    ) },
    /*loading_status*/
    n[9]
  ];
  let s = {};
  for (let i = 0; i < l.length; i += 1)
    s = on(s, l[i]);
  return e = new tn({ props: s }), {
    c() {
      ve(e.$$.fragment);
    },
    m(i, o) {
      ye(e, i, o), t = !0;
    },
    p(i, o) {
      const f = o & /*gradio, loading_status*/
      514 ? cn(l, [
        o & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          i[1].autoscroll
        ) },
        o & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          i[1].i18n
        ) },
        o & /*loading_status*/
        512 && un(
          /*loading_status*/
          i[9]
        )
      ]) : {};
      e.$set(f);
    },
    i(i) {
      t || (K(e.$$.fragment, i), t = !0);
    },
    o(i) {
      le(e.$$.fragment, i), t = !1;
    },
    d(i) {
      ke(e, i);
    }
  };
}
function hn(n) {
  let e;
  return {
    c() {
      e = ct(
        /*label*/
        n[2]
      );
    },
    m(t, l) {
      ie(t, e, l);
    },
    p(t, l) {
      l & /*label*/
      4 && ut(
        e,
        /*label*/
        t[2]
      );
    },
    d(t) {
      t && ne(e);
    }
  };
}
function wn(n) {
  let e, t;
  return {
    c() {
      e = new sn(!1), t = _n(), e.a = t;
    },
    m(l, s) {
      e.m(
        /*_value*/
        n[14],
        l,
        s
      ), ie(l, t, s);
    },
    p(l, s) {
      s & /*_value*/
      16384 && e.p(
        /*_value*/
        l[14]
      );
    },
    d(l) {
      l && (ne(t), e.d());
    }
  };
}
function pn(n) {
  let e;
  return {
    c() {
      e = ct(
        /*value*/
        n[0]
      );
    },
    m(t, l) {
      ie(t, e, l);
    },
    p(t, l) {
      l & /*value*/
      1 && ut(
        e,
        /*value*/
        t[0]
      );
    },
    d(t) {
      t && ne(e);
    }
  };
}
function vn(n) {
  let e, t, l, s, i, o, f, a, r, _ = (
    /*loading_status*/
    n[9] && lt(n)
  );
  l = new ml({
    props: {
      show_label: (
        /*show_label*/
        n[6]
      ),
      info: void 0,
      $$slots: { default: [hn] },
      $$scope: { ctx: n }
    }
  });
  function u(d, y) {
    return (
      /*is_being_edited*/
      d[13] ? pn : wn
    );
  }
  let b = u(n), c = b(n);
  return {
    c() {
      _ && _.c(), e = tt(), t = et("label"), ve(l.$$.fragment), s = tt(), i = et("div"), c.c(), O(i, "data-testid", "textbox"), O(i, "contenteditable", "true"), O(i, "class", "text-container svelte-15aeqxz"), O(i, "role", "textbox"), O(i, "tabindex", "0"), O(i, "dir", o = /*rtl*/
      n[11] ? "rtl" : "ltr"), ge(i, "disabled", !/*interactive*/
      n[10]), O(t, "class", "svelte-15aeqxz"), ge(t, "container", yn);
    },
    m(d, y) {
      _ && _.m(d, y), ie(d, e, y), ie(d, t, y), ye(l, t, null), $e(t, s), $e(t, i), c.m(i, null), n[19](i), f = !0, a || (r = [
        be(
          i,
          "keypress",
          /*handle_keypress*/
          n[15]
        ),
        be(
          i,
          "blur",
          /*handle_blur*/
          n[16]
        ),
        be(
          i,
          "focus",
          /*handle_focus*/
          n[17]
        )
      ], a = !0);
    },
    p(d, y) {
      /*loading_status*/
      d[9] ? _ ? (_.p(d, y), y & /*loading_status*/
      512 && K(_, 1)) : (_ = lt(d), _.c(), K(_, 1), _.m(e.parentNode, e)) : _ && (dn(), le(_, 1, 1, () => {
        _ = null;
      }), rn());
      const v = {};
      y & /*show_label*/
      64 && (v.show_label = /*show_label*/
      d[6]), y & /*$$scope, label*/
      2097156 && (v.$$scope = { dirty: y, ctx: d }), l.$set(v), b === (b = u(d)) && c ? c.p(d, y) : (c.d(1), c = b(d), c && (c.c(), c.m(i, null))), (!f || y & /*rtl*/
      2048 && o !== (o = /*rtl*/
      d[11] ? "rtl" : "ltr")) && O(i, "dir", o), (!f || y & /*interactive*/
      1024) && ge(i, "disabled", !/*interactive*/
      d[10]);
    },
    i(d) {
      f || (K(_), K(l.$$.fragment, d), f = !0);
    },
    o(d) {
      le(_), le(l.$$.fragment, d), f = !1;
    },
    d(d) {
      d && (ne(e), ne(t)), _ && _.d(d), ke(l), c.d(), n[19](null), a = !1, bn(r);
    }
  };
}
function kn(n) {
  let e, t;
  return e = new At({
    props: {
      visible: (
        /*visible*/
        n[5]
      ),
      elem_id: (
        /*elem_id*/
        n[3]
      ),
      elem_classes: (
        /*elem_classes*/
        n[4]
      ),
      scale: (
        /*scale*/
        n[7]
      ),
      min_width: (
        /*min_width*/
        n[8]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [vn] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      ve(e.$$.fragment);
    },
    m(l, s) {
      ye(e, l, s), t = !0;
    },
    p(l, [s]) {
      const i = {};
      s & /*visible*/
      32 && (i.visible = /*visible*/
      l[5]), s & /*elem_id*/
      8 && (i.elem_id = /*elem_id*/
      l[3]), s & /*elem_classes*/
      16 && (i.elem_classes = /*elem_classes*/
      l[4]), s & /*scale*/
      128 && (i.scale = /*scale*/
      l[7]), s & /*min_width*/
      256 && (i.min_width = /*min_width*/
      l[8]), s & /*$$scope, rtl, el, interactive, value, is_being_edited, _value, show_label, label, gradio, loading_status*/
      2129479 && (i.$$scope = { dirty: s, ctx: l }), e.$set(i);
    },
    i(l) {
      t || (K(e.$$.fragment, l), t = !0);
    },
    o(l) {
      le(e.$$.fragment, l), t = !1;
    },
    d(l) {
      ke(e, l);
    }
  };
}
const yn = !0;
function Tn(n, e, t) {
  let { gradio: l } = e, { label: s = "Textbox" } = e, { elem_id: i = "" } = e, { elem_classes: o = [] } = e, { visible: f = !0 } = e, { value: a = "" } = e, { show_label: r } = e, { scale: _ = null } = e, { min_width: u = void 0 } = e, { loading_status: b = void 0 } = e, { value_is_output: c = !1 } = e, { interactive: d } = e, { rtl: y = !1 } = e, v;
  function F() {
    l.dispatch("change"), c || l.dispatch("input");
  }
  async function q(k) {
    await he(), k.key === "Enter" && (k.preventDefault(), l.dispatch("submit"));
  }
  let m = !1, z = "";
  async function h() {
    await he(), d && (t(0, a = v.innerText), t(13, m = !1), t(12, v.innerText = "", v));
  }
  async function $() {
    if (await he(), !d) {
      v.blur();
      return;
    }
    t(13, m = !0);
  }
  function R(k) {
    an[k ? "unshift" : "push"](() => {
      v = k, t(12, v);
    });
  }
  return n.$$set = (k) => {
    "gradio" in k && t(1, l = k.gradio), "label" in k && t(2, s = k.label), "elem_id" in k && t(3, i = k.elem_id), "elem_classes" in k && t(4, o = k.elem_classes), "visible" in k && t(5, f = k.visible), "value" in k && t(0, a = k.value), "show_label" in k && t(6, r = k.show_label), "scale" in k && t(7, _ = k.scale), "min_width" in k && t(8, u = k.min_width), "loading_status" in k && t(9, b = k.loading_status), "value_is_output" in k && t(18, c = k.value_is_output), "interactive" in k && t(10, d = k.interactive), "rtl" in k && t(11, y = k.rtl);
  }, n.$$.update = () => {
    n.$$.dirty & /*value*/
    1 && a === null && t(0, a = ""), n.$$.dirty & /*value*/
    1 && t(14, z = nn.bbcodeToHtml(a || "")), n.$$.dirty & /*value*/
    1 && F();
  }, [
    a,
    l,
    s,
    i,
    o,
    f,
    r,
    _,
    u,
    b,
    d,
    y,
    v,
    m,
    z,
    q,
    h,
    $,
    c,
    R
  ];
}
class zn extends fn {
  constructor(e) {
    super(), mn(this, e, Tn, kn, gn, {
      gradio: 1,
      label: 2,
      elem_id: 3,
      elem_classes: 4,
      visible: 5,
      value: 0,
      show_label: 6,
      scale: 7,
      min_width: 8,
      loading_status: 9,
      value_is_output: 18,
      interactive: 10,
      rtl: 11
    });
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), E();
  }
  get label() {
    return this.$$.ctx[2];
  }
  set label(e) {
    this.$$set({ label: e }), E();
  }
  get elem_id() {
    return this.$$.ctx[3];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), E();
  }
  get elem_classes() {
    return this.$$.ctx[4];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), E();
  }
  get visible() {
    return this.$$.ctx[5];
  }
  set visible(e) {
    this.$$set({ visible: e }), E();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), E();
  }
  get show_label() {
    return this.$$.ctx[6];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), E();
  }
  get scale() {
    return this.$$.ctx[7];
  }
  set scale(e) {
    this.$$set({ scale: e }), E();
  }
  get min_width() {
    return this.$$.ctx[8];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), E();
  }
  get loading_status() {
    return this.$$.ctx[9];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), E();
  }
  get value_is_output() {
    return this.$$.ctx[18];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), E();
  }
  get interactive() {
    return this.$$.ctx[10];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), E();
  }
  get rtl() {
    return this.$$.ctx[11];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), E();
  }
}
export {
  zn as default
};
