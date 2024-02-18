const {
  SvelteComponent: yl,
  append: se,
  attr: U,
  create_slot: Cl,
  destroy_each: ql,
  detach: fe,
  element: de,
  empty: Sl,
  ensure_array_like: tt,
  get_all_dirty_from_scope: Tl,
  get_slot_changes: Ll,
  init: jl,
  insert: _e,
  safe_not_equal: Fl,
  set_data: Je,
  space: Me,
  text: Ke,
  toggle_class: V,
  transition_in: Hl,
  transition_out: Ml,
  update_slot_base: Nl
} = window.__gradio__svelte__internal;
function lt(l, e, t) {
  const n = l.slice();
  return n[8] = e[t][0], n[9] = e[t][1], n[11] = t, n;
}
function nt(l) {
  let e, t, n, i, o, s, f = tt(Object.entries(
    /*_color_map*/
    l[4]
  )), a = [];
  for (let _ = 0; _ < f.length; _ += 1)
    a[_] = it(lt(l, f, _));
  return {
    c() {
      e = de("span"), e.textContent = "·", t = Me(), n = de("div"), i = de("span"), o = Ke(
        /*legend_label*/
        l[3]
      ), s = Me();
      for (let _ = 0; _ < a.length; _ += 1)
        a[_].c();
      U(e, "class", "legend-separator svelte-vm3q5z"), V(e, "hide", !/*show_legend*/
      l[1] || !/*show_label*/
      l[0]), V(
        e,
        "has-info",
        /*info*/
        l[5] != null
      ), U(i, "class", "svelte-vm3q5z"), V(i, "hide", !/*show_legend_label*/
      l[2]), V(
        i,
        "has-info",
        /*info*/
        l[5] != null
      ), U(n, "class", "category-legend svelte-vm3q5z"), U(n, "data-testid", "highlighted-text:category-legend"), V(n, "hide", !/*show_legend*/
      l[1]);
    },
    m(_, r) {
      _e(_, e, r), _e(_, t, r), _e(_, n, r), se(n, i), se(i, o), se(n, s);
      for (let u = 0; u < a.length; u += 1)
        a[u] && a[u].m(n, null);
    },
    p(_, r) {
      if (r & /*show_legend, show_label*/
      3 && V(e, "hide", !/*show_legend*/
      _[1] || !/*show_label*/
      _[0]), r & /*info*/
      32 && V(
        e,
        "has-info",
        /*info*/
        _[5] != null
      ), r & /*legend_label*/
      8 && Je(
        o,
        /*legend_label*/
        _[3]
      ), r & /*show_legend_label*/
      4 && V(i, "hide", !/*show_legend_label*/
      _[2]), r & /*info*/
      32 && V(
        i,
        "has-info",
        /*info*/
        _[5] != null
      ), r & /*Object, _color_map, info*/
      48) {
        f = tt(Object.entries(
          /*_color_map*/
          _[4]
        ));
        let u;
        for (u = 0; u < f.length; u += 1) {
          const c = lt(_, f, u);
          a[u] ? a[u].p(c, r) : (a[u] = it(c), a[u].c(), a[u].m(n, null));
        }
        for (; u < a.length; u += 1)
          a[u].d(1);
        a.length = f.length;
      }
      r & /*show_legend*/
      2 && V(n, "hide", !/*show_legend*/
      _[1]);
    },
    d(_) {
      _ && (fe(e), fe(t), fe(n)), ql(a, _);
    }
  };
}
function it(l) {
  let e, t = (
    /*category*/
    l[8] + ""
  ), n, i, o;
  return {
    c() {
      e = de("div"), n = Ke(t), i = Me(), U(e, "class", "category-label svelte-vm3q5z"), U(e, "style", o = "background-color:" + /*color*/
      l[9].secondary), V(
        e,
        "has-info",
        /*info*/
        l[5] != null
      );
    },
    m(s, f) {
      _e(s, e, f), se(e, n), se(e, i);
    },
    p(s, f) {
      f & /*_color_map*/
      16 && t !== (t = /*category*/
      s[8] + "") && Je(n, t), f & /*_color_map*/
      16 && o !== (o = "background-color:" + /*color*/
      s[9].secondary) && U(e, "style", o), f & /*info*/
      32 && V(
        e,
        "has-info",
        /*info*/
        s[5] != null
      );
    },
    d(s) {
      s && fe(e);
    }
  };
}
function ot(l) {
  let e, t;
  return {
    c() {
      e = de("div"), t = Ke(
        /*info*/
        l[5]
      ), U(e, "class", "title-with-highlights-info svelte-vm3q5z");
    },
    m(n, i) {
      _e(n, e, i), se(e, t);
    },
    p(n, i) {
      i & /*info*/
      32 && Je(
        t,
        /*info*/
        n[5]
      );
    },
    d(n) {
      n && fe(e);
    }
  };
}
function Vl(l) {
  let e, t, n, i = Object.keys(
    /*_color_map*/
    l[4]
  ).length !== 0, o, s, f;
  const a = (
    /*#slots*/
    l[7].default
  ), _ = Cl(
    a,
    l,
    /*$$scope*/
    l[6],
    null
  );
  let r = i && nt(l), u = (
    /*info*/
    l[5] && ot(l)
  );
  return {
    c() {
      e = de("div"), t = de("span"), _ && _.c(), n = Me(), r && r.c(), o = Me(), u && u.c(), s = Sl(), U(t, "data-testid", "block-info"), U(t, "class", "svelte-vm3q5z"), V(t, "sr-only", !/*show_label*/
      l[0]), V(t, "hide", !/*show_label*/
      l[0]), V(
        t,
        "has-info",
        /*info*/
        l[5] != null
      ), U(e, "class", "title-container svelte-vm3q5z");
    },
    m(c, m) {
      _e(c, e, m), se(e, t), _ && _.m(t, null), se(e, n), r && r.m(e, null), _e(c, o, m), u && u.m(c, m), _e(c, s, m), f = !0;
    },
    p(c, [m]) {
      _ && _.p && (!f || m & /*$$scope*/
      64) && Nl(
        _,
        a,
        c,
        /*$$scope*/
        c[6],
        f ? Ll(
          a,
          /*$$scope*/
          c[6],
          m,
          null
        ) : Tl(
          /*$$scope*/
          c[6]
        ),
        null
      ), (!f || m & /*show_label*/
      1) && V(t, "sr-only", !/*show_label*/
      c[0]), (!f || m & /*show_label*/
      1) && V(t, "hide", !/*show_label*/
      c[0]), (!f || m & /*info*/
      32) && V(
        t,
        "has-info",
        /*info*/
        c[5] != null
      ), m & /*_color_map*/
      16 && (i = Object.keys(
        /*_color_map*/
        c[4]
      ).length !== 0), i ? r ? r.p(c, m) : (r = nt(c), r.c(), r.m(e, null)) : r && (r.d(1), r = null), /*info*/
      c[5] ? u ? u.p(c, m) : (u = ot(c), u.c(), u.m(s.parentNode, s)) : u && (u.d(1), u = null);
    },
    i(c) {
      f || (Hl(_, c), f = !0);
    },
    o(c) {
      Ml(_, c), f = !1;
    },
    d(c) {
      c && (fe(e), fe(o), fe(s)), _ && _.d(c), r && r.d(), u && u.d(c);
    }
  };
}
function zl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { show_label: o = !0 } = e, { show_legend: s = !0 } = e, { show_legend_label: f = !0 } = e, { legend_label: a = "Highlights:" } = e, { _color_map: _ = {} } = e, { info: r = void 0 } = e;
  return l.$$set = (u) => {
    "show_label" in u && t(0, o = u.show_label), "show_legend" in u && t(1, s = u.show_legend), "show_legend_label" in u && t(2, f = u.show_legend_label), "legend_label" in u && t(3, a = u.legend_label), "_color_map" in u && t(4, _ = u._color_map), "info" in u && t(5, r = u.info), "$$scope" in u && t(6, i = u.$$scope);
  }, [
    o,
    s,
    f,
    a,
    _,
    r,
    i,
    n
  ];
}
class El extends yl {
  constructor(e) {
    super(), jl(this, e, zl, Vl, Fl, {
      show_label: 0,
      show_legend: 1,
      show_legend_label: 2,
      legend_label: 3,
      _color_map: 4,
      info: 5
    });
  }
}
function Re() {
}
const Rl = (l) => l;
function Dl(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const tl = typeof window < "u";
let st = tl ? () => window.performance.now() : () => Date.now(), ll = tl ? (l) => requestAnimationFrame(l) : Re;
const Ce = /* @__PURE__ */ new Set();
function nl(l) {
  Ce.forEach((e) => {
    e.c(l) || (Ce.delete(e), e.f());
  }), Ce.size !== 0 && ll(nl);
}
function Bl(l) {
  let e;
  return Ce.size === 0 && ll(nl), {
    promise: new Promise((t) => {
      Ce.add(e = { c: l, f: t });
    }),
    abort() {
      Ce.delete(e);
    }
  };
}
function ft(l, { delay: e = 0, duration: t = 400, easing: n = Rl } = {}) {
  const i = +getComputedStyle(l).opacity;
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (o) => `opacity: ${o * i}`
  };
}
const ve = [];
function Pl(l, e = Re) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(f) {
    if (Dl(l, f) && (l = f, t)) {
      const a = !ve.length;
      for (const _ of n)
        _[1](), ve.push(_, l);
      if (a) {
        for (let _ = 0; _ < ve.length; _ += 2)
          ve[_][0](ve[_ + 1]);
        ve.length = 0;
      }
    }
  }
  function o(f) {
    i(f(l));
  }
  function s(f, a = Re) {
    const _ = [f, a];
    return n.add(_), n.size === 1 && (t = e(i, o) || Re), f(l), () => {
      n.delete(_), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: o, subscribe: s };
}
function _t(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Ye(l, e, t, n) {
  if (typeof t == "number" || _t(t)) {
    const i = n - t, o = (t - e) / (l.dt || 1 / 60), s = l.opts.stiffness * i, f = l.opts.damping * o, a = (s - f) * l.inv_mass, _ = (o + a) * l.dt;
    return Math.abs(_) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, _t(t) ? new Date(t.getTime() + _) : t + _);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, o) => Ye(l, e[o], t[o], n[o])
      );
    if (typeof t == "object") {
      const i = {};
      for (const o in t)
        i[o] = Ye(l, e[o], t[o], n[o]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function at(l, e = {}) {
  const t = Pl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: o = 0.01 } = e;
  let s, f, a, _ = l, r = l, u = 1, c = 0, m = !1;
  function k(T, S = {}) {
    r = T;
    const y = a = {};
    return l == null || S.hard || L.stiffness >= 1 && L.damping >= 1 ? (m = !0, s = st(), _ = T, t.set(l = r), Promise.resolve()) : (S.soft && (c = 1 / ((S.soft === !0 ? 0.5 : +S.soft) * 60), u = 0), f || (s = st(), m = !1, f = Bl((d) => {
      if (m)
        return m = !1, f = null, !1;
      u = Math.min(u + c, 1);
      const C = {
        inv_mass: u,
        opts: L,
        settled: !0,
        dt: (d - s) * 60 / 1e3
      }, j = Ye(C, _, l, r);
      return s = d, _ = l, t.set(l = j), C.settled && (f = null), !C.settled;
    })), new Promise((d) => {
      f.promise.then(() => {
        y === a && d();
      });
    }));
  }
  const L = {
    set: k,
    update: (T, S) => k(T(r, l), S),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: o
  };
  return L;
}
const {
  SvelteComponent: Zl,
  append: Ol,
  attr: le,
  detach: Al,
  init: Wl,
  insert: Il,
  noop: We,
  safe_not_equal: Ul,
  svg_element: rt
} = window.__gradio__svelte__internal;
function Xl(l) {
  let e, t;
  return {
    c() {
      e = rt("svg"), t = rt("polyline"), le(t, "points", "20 6 9 17 4 12"), le(e, "xmlns", "http://www.w3.org/2000/svg"), le(e, "viewBox", "2 0 20 20"), le(e, "fill", "none"), le(e, "stroke", "currentColor"), le(e, "stroke-width", "3"), le(e, "stroke-linecap", "round"), le(e, "stroke-linejoin", "round");
    },
    m(n, i) {
      Il(n, e, i), Ol(e, t);
    },
    p: We,
    i: We,
    o: We,
    d(n) {
      n && Al(e);
    }
  };
}
class il extends Zl {
  constructor(e) {
    super(), Wl(this, e, null, Xl, Ul, {});
  }
}
const {
  SvelteComponent: Yl,
  append: ut,
  attr: re,
  detach: Gl,
  init: Jl,
  insert: Kl,
  noop: Ie,
  safe_not_equal: Ql,
  svg_element: Ue
} = window.__gradio__svelte__internal;
function xl(l) {
  let e, t, n;
  return {
    c() {
      e = Ue("svg"), t = Ue("path"), n = Ue("path"), re(t, "fill", "currentColor"), re(t, "d", "M28 10v18H10V10h18m0-2H10a2 2 0 0 0-2 2v18a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2Z"), re(n, "fill", "currentColor"), re(n, "d", "M4 18H2V4a2 2 0 0 1 2-2h14v2H4Z"), re(e, "xmlns", "http://www.w3.org/2000/svg"), re(e, "viewBox", "0 0 33 33"), re(e, "color", "currentColor");
    },
    m(i, o) {
      Kl(i, e, o), ut(e, t), ut(e, n);
    },
    p: Ie,
    i: Ie,
    o: Ie,
    d(i) {
      i && Gl(e);
    }
  };
}
class $l extends Yl {
  constructor(e) {
    super(), Jl(this, e, null, xl, Ql, {});
  }
}
const {
  SvelteComponent: en,
  add_render_callback: tn,
  append: ln,
  attr: ue,
  check_outros: nn,
  create_bidirectional_transition: ct,
  create_component: ol,
  destroy_component: sl,
  detach: fl,
  element: _l,
  group_outros: on,
  init: sn,
  insert: al,
  listen: fn,
  mount_component: rl,
  safe_not_equal: _n,
  space: an,
  toggle_class: dt,
  transition_in: Fe,
  transition_out: De
} = window.__gradio__svelte__internal, { onDestroy: rn } = window.__gradio__svelte__internal;
function mt(l) {
  let e, t, n, i;
  return t = new il({}), {
    c() {
      e = _l("span"), ol(t.$$.fragment), ue(e, "class", "check svelte-qjb524"), ue(e, "aria-roledescription", "Value copied"), ue(e, "aria-label", "Copied");
    },
    m(o, s) {
      al(o, e, s), rl(t, e, null), i = !0;
    },
    i(o) {
      i || (Fe(t.$$.fragment, o), o && tn(() => {
        i && (n || (n = ct(e, ft, {}, !0)), n.run(1));
      }), i = !0);
    },
    o(o) {
      De(t.$$.fragment, o), o && (n || (n = ct(e, ft, {}, !1)), n.run(0)), i = !1;
    },
    d(o) {
      o && fl(e), sl(t), o && n && n.end();
    }
  };
}
function un(l) {
  let e, t, n, i, o, s;
  t = new $l({});
  let f = (
    /*copied*/
    l[0] && mt()
  );
  return {
    c() {
      e = _l("button"), ol(t.$$.fragment), n = an(), f && f.c(), ue(e, "title", "Copy text to clipboard"), ue(e, "aria-roledescription", "Copy value"), ue(e, "aria-label", "Copy"), ue(e, "class", "svelte-qjb524"), dt(
        e,
        "copied",
        /*copied*/
        l[0]
      );
    },
    m(a, _) {
      al(a, e, _), rl(t, e, null), ln(e, n), f && f.m(e, null), i = !0, o || (s = fn(
        e,
        "click",
        /*handle_copy*/
        l[1]
      ), o = !0);
    },
    p(a, [_]) {
      /*copied*/
      a[0] ? f ? _ & /*copied*/
      1 && Fe(f, 1) : (f = mt(), f.c(), Fe(f, 1), f.m(e, null)) : f && (on(), De(f, 1, 1, () => {
        f = null;
      }), nn()), (!i || _ & /*copied*/
      1) && dt(
        e,
        "copied",
        /*copied*/
        a[0]
      );
    },
    i(a) {
      i || (Fe(t.$$.fragment, a), Fe(f), i = !0);
    },
    o(a) {
      De(t.$$.fragment, a), De(f), i = !1;
    },
    d(a) {
      a && fl(e), sl(t), f && f.d(), o = !1, s();
    }
  };
}
function cn(l, e, t) {
  let n = !1, { value: i } = e, o;
  function s() {
    t(0, n = !0), o && clearTimeout(o), o = setTimeout(
      () => {
        t(0, n = !1);
      },
      2e3
    );
  }
  async function f() {
    "clipboard" in navigator && (await navigator.clipboard.writeText(i), s());
  }
  return rn(() => {
    o && clearTimeout(o);
  }), l.$$set = (a) => {
    "value" in a && t(2, i = a.value);
  }, [n, f, i];
}
class dn extends en {
  constructor(e) {
    super(), sn(this, e, cn, un, _n, { value: 2 });
  }
}
const {
  SvelteComponent: mn,
  attr: Ve,
  create_component: gn,
  destroy_component: hn,
  detach: bn,
  element: wn,
  init: vn,
  insert: pn,
  listen: kn,
  mount_component: yn,
  noop: Cn,
  safe_not_equal: qn,
  transition_in: Sn,
  transition_out: Tn
} = window.__gradio__svelte__internal, { createEventDispatcher: Ln } = window.__gradio__svelte__internal;
function jn(l) {
  let e, t, n, i, o;
  return t = new il({}), {
    c() {
      e = wn("button"), gn(t.$$.fragment), Ve(e, "title", "Remove highlights"), Ve(e, "aria-roledescription", "Remove highlights"), Ve(e, "aria-label", "Remove highlights"), Ve(e, "class", "svelte-1ga0gmr");
    },
    m(s, f) {
      pn(s, e, f), yn(t, e, null), n = !0, i || (o = kn(
        e,
        "click",
        /*click_handler*/
        l[1]
      ), i = !0);
    },
    p: Cn,
    i(s) {
      n || (Sn(t.$$.fragment, s), n = !0);
    },
    o(s) {
      Tn(t.$$.fragment, s), n = !1;
    },
    d(s) {
      s && bn(e), hn(t), i = !1, o();
    }
  };
}
function Fn(l) {
  const e = Ln();
  return [e, () => e("clear")];
}
class Hn extends mn {
  constructor(e) {
    super(), vn(this, e, Fn, jn, qn, {});
  }
}
const {
  SvelteComponent: Mn,
  append: Nn,
  attr: Vn,
  check_outros: gt,
  create_component: ul,
  destroy_component: cl,
  detach: zn,
  element: En,
  group_outros: ht,
  init: Rn,
  insert: Dn,
  mount_component: dl,
  noop: Bn,
  safe_not_equal: Pn,
  space: Zn,
  transition_in: ie,
  transition_out: pe
} = window.__gradio__svelte__internal, { createEventDispatcher: On } = window.__gradio__svelte__internal;
function bt(l) {
  let e, t;
  return e = new Hn({}), e.$on(
    "clear",
    /*clear_handler*/
    l[4]
  ), {
    c() {
      ul(e.$$.fragment);
    },
    m(n, i) {
      dl(e, n, i), t = !0;
    },
    p: Bn,
    i(n) {
      t || (ie(e.$$.fragment, n), t = !0);
    },
    o(n) {
      pe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      cl(e, n);
    }
  };
}
function wt(l) {
  let e, t;
  return e = new dn({ props: { value: (
    /*value*/
    l[0]
  ) } }), {
    c() {
      ul(e.$$.fragment);
    },
    m(n, i) {
      dl(e, n, i), t = !0;
    },
    p(n, i) {
      const o = {};
      i & /*value*/
      1 && (o.value = /*value*/
      n[0]), e.$set(o);
    },
    i(n) {
      t || (ie(e.$$.fragment, n), t = !0);
    },
    o(n) {
      pe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      cl(e, n);
    }
  };
}
function An(l) {
  let e, t, n, i = (
    /*show_remove_tags_button*/
    l[2] && bt(l)
  ), o = (
    /*show_copy_button*/
    l[1] && wt(l)
  );
  return {
    c() {
      e = En("div"), i && i.c(), t = Zn(), o && o.c(), Vn(e, "class", "svelte-1bqqv16");
    },
    m(s, f) {
      Dn(s, e, f), i && i.m(e, null), Nn(e, t), o && o.m(e, null), n = !0;
    },
    p(s, [f]) {
      /*show_remove_tags_button*/
      s[2] ? i ? (i.p(s, f), f & /*show_remove_tags_button*/
      4 && ie(i, 1)) : (i = bt(s), i.c(), ie(i, 1), i.m(e, t)) : i && (ht(), pe(i, 1, 1, () => {
        i = null;
      }), gt()), /*show_copy_button*/
      s[1] ? o ? (o.p(s, f), f & /*show_copy_button*/
      2 && ie(o, 1)) : (o = wt(s), o.c(), ie(o, 1), o.m(e, null)) : o && (ht(), pe(o, 1, 1, () => {
        o = null;
      }), gt());
    },
    i(s) {
      n || (ie(i), ie(o), n = !0);
    },
    o(s) {
      pe(i), pe(o), n = !1;
    },
    d(s) {
      s && zn(e), i && i.d(), o && o.d();
    }
  };
}
function Wn(l, e, t) {
  let { value: n } = e, { show_copy_button: i = !1 } = e, { show_remove_tags_button: o = !1 } = e;
  const s = On(), f = () => s("clear");
  return l.$$set = (a) => {
    "value" in a && t(0, n = a.value), "show_copy_button" in a && t(1, i = a.show_copy_button), "show_remove_tags_button" in a && t(2, o = a.show_remove_tags_button);
  }, [n, i, o, s, f];
}
class In extends Mn {
  constructor(e) {
    super(), Rn(this, e, Wn, An, Pn, {
      value: 0,
      show_copy_button: 1,
      show_remove_tags_button: 2
    });
  }
}
const vt = [
  "red",
  "green",
  "blue",
  "yellow",
  "purple",
  "teal",
  "orange",
  "cyan",
  "lime",
  "pink"
], Un = [
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
], pt = {
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
}, kt = Un.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: pt[e][t],
      secondary: pt[e][n]
    }
  }),
  {}
), Xn = (l) => vt[l % vt.length];
function yt(l, e, t) {
  if (!t) {
    var n = document.createElement("canvas");
    t = n.getContext("2d");
  }
  t.fillStyle = l, t.fillRect(0, 0, 1, 1);
  const [i, o, s] = t.getImageData(0, 0, 1, 1).data;
  return t.clearRect(0, 0, 1, 1), `rgba(${i}, ${o}, ${s}, ${255 / e})`;
}
function Yn(l, e, t) {
  var n = {};
  for (const i in l) {
    const o = l[i].trim();
    o in kt ? n[i] = kt[o] : n[i] = {
      primary: e ? yt(l[i], 1, t) : l[i],
      secondary: e ? yt(l[i], 0.5, t) : l[i]
    };
  }
  return n;
}
function Gn(l, e) {
  let t = [], n = null, i = null;
  for (const [o, s] of l)
    e === "empty" && s === null || e === "equal" && i === s ? n = n ? n + o : o : (n !== null && t.push([n, i]), n = o, i = s);
  return n !== null && t.push([n, i]), t;
}
function Jn(l) {
  const e = window.getSelection();
  if (e.rangeCount > 0) {
    const t = document.createRange();
    return t.setStart(l, 0), e.anchorNode !== null && t.setEnd(e.anchorNode, e.anchorOffset), t.toString().length;
  }
  return -1;
}
function Kn(l, e) {
  var t = document.createTreeWalker(l, NodeFilter.SHOW_TEXT), n = t.nextNode();
  if (!n || !n.textContent)
    return null;
  for (var i = n.textContent.length; i < e; )
    if (n = t.nextNode(), n && n.textContent)
      i += n.textContent.length;
    else
      return null;
  var o = n.textContent.length - (i - e);
  return { node: n, offset: o };
}
const {
  SvelteComponent: Qn,
  add_render_callback: ml,
  append: Ct,
  attr: X,
  binding_callbacks: qt,
  bubble: je,
  create_component: St,
  destroy_component: Tt,
  detach: Pe,
  element: Qe,
  init: xn,
  insert: Ze,
  listen: x,
  mount_component: Lt,
  run_all: $n,
  safe_not_equal: ei,
  set_data: ti,
  space: jt,
  text: li,
  toggle_class: Ft,
  transition_in: Ht,
  transition_out: Mt
} = window.__gradio__svelte__internal, { beforeUpdate: ni, afterUpdate: ii, createEventDispatcher: oi } = window.__gradio__svelte__internal;
function si(l) {
  let e;
  return {
    c() {
      e = li(
        /*label*/
        l[0]
      );
    },
    m(t, n) {
      Ze(t, e, n);
    },
    p(t, n) {
      n[0] & /*label*/
      1 && ti(
        e,
        /*label*/
        t[0]
      );
    },
    d(t) {
      t && Pe(e);
    }
  };
}
function fi(l) {
  let e, t, n;
  return {
    c() {
      e = Qe("div"), X(e, "class", "textfield svelte-1atky07"), X(e, "data-testid", "highlighted-textbox"), X(e, "contenteditable", "true"), X(e, "role", "textbox"), X(e, "tabindex", "0"), /*el_text*/
      (l[11] === void 0 || /*marked_el_text*/
      l[12] === void 0) && ml(() => (
        /*div_input_handler_1*/
        l[29].call(e)
      ));
    },
    m(i, o) {
      Ze(i, e, o), l[28](e), /*el_text*/
      l[11] !== void 0 && (e.textContent = /*el_text*/
      l[11]), /*marked_el_text*/
      l[12] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[12]), t || (n = [
        x(
          e,
          "input",
          /*div_input_handler_1*/
          l[29]
        ),
        x(
          e,
          "blur",
          /*blur_handler*/
          l[21]
        ),
        x(
          e,
          "keypress",
          /*keypress_handler*/
          l[22]
        ),
        x(
          e,
          "select",
          /*select_handler*/
          l[23]
        ),
        x(
          e,
          "scroll",
          /*scroll_handler*/
          l[24]
        ),
        x(
          e,
          "input",
          /*handle_change*/
          l[16]
        ),
        x(
          e,
          "focus",
          /*focus_handler*/
          l[25]
        ),
        x(
          e,
          "change",
          /*handle_change*/
          l[16]
        )
      ], t = !0);
    },
    p(i, o) {
      o[0] & /*el_text*/
      2048 && /*el_text*/
      i[11] !== e.textContent && (e.textContent = /*el_text*/
      i[11]), o[0] & /*marked_el_text*/
      4096 && /*marked_el_text*/
      i[12] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[12]);
    },
    d(i) {
      i && Pe(e), l[28](null), t = !1, $n(n);
    }
  };
}
function _i(l) {
  let e, t, n;
  return {
    c() {
      e = Qe("div"), X(e, "class", "textfield svelte-1atky07"), X(e, "data-testid", "highlighted-textbox"), X(e, "contenteditable", "false"), /*el_text*/
      (l[11] === void 0 || /*marked_el_text*/
      l[12] === void 0) && ml(() => (
        /*div_input_handler*/
        l[27].call(e)
      ));
    },
    m(i, o) {
      Ze(i, e, o), l[26](e), /*el_text*/
      l[11] !== void 0 && (e.textContent = /*el_text*/
      l[11]), /*marked_el_text*/
      l[12] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[12]), t || (n = x(
        e,
        "input",
        /*div_input_handler*/
        l[27]
      ), t = !0);
    },
    p(i, o) {
      o[0] & /*el_text*/
      2048 && /*el_text*/
      i[11] !== e.textContent && (e.textContent = /*el_text*/
      i[11]), o[0] & /*marked_el_text*/
      4096 && /*marked_el_text*/
      i[12] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[12]);
    },
    d(i) {
      i && Pe(e), l[26](null), t = !1, n();
    }
  };
}
function ai(l) {
  let e, t, n, i, o, s;
  t = new El({
    props: {
      show_label: (
        /*show_label*/
        l[3]
      ),
      show_legend: (
        /*show_legend*/
        l[4]
      ),
      show_legend_label: (
        /*show_legend_label*/
        l[5]
      ),
      legend_label: (
        /*legend_label*/
        l[1]
      ),
      _color_map: (
        /*_color_map*/
        l[13]
      ),
      info: (
        /*info*/
        l[2]
      ),
      $$slots: { default: [si] },
      $$scope: { ctx: l }
    }
  }), i = new In({
    props: {
      show_copy_button: (
        /*show_copy_button*/
        l[7]
      ),
      show_remove_tags_button: (
        /*show_remove_tags_button*/
        l[8] && !/*tags_removed*/
        l[14]
      ),
      value: (
        /*tagged_text*/
        l[15]
      )
    }
  }), i.$on(
    "clear",
    /*handle_remove_tags*/
    l[17]
  );
  function f(r, u) {
    return (
      /*disabled*/
      r[9] ? _i : fi
    );
  }
  let a = f(l), _ = a(l);
  return {
    c() {
      e = Qe("label"), St(t.$$.fragment), n = jt(), St(i.$$.fragment), o = jt(), _.c(), X(e, "for", "highlighted-textbox"), X(e, "class", "svelte-1atky07"), Ft(
        e,
        "container",
        /*container*/
        l[6]
      );
    },
    m(r, u) {
      Ze(r, e, u), Lt(t, e, null), Ct(e, n), Lt(i, e, null), Ct(e, o), _.m(e, null), s = !0;
    },
    p(r, u) {
      const c = {};
      u[0] & /*show_label*/
      8 && (c.show_label = /*show_label*/
      r[3]), u[0] & /*show_legend*/
      16 && (c.show_legend = /*show_legend*/
      r[4]), u[0] & /*show_legend_label*/
      32 && (c.show_legend_label = /*show_legend_label*/
      r[5]), u[0] & /*legend_label*/
      2 && (c.legend_label = /*legend_label*/
      r[1]), u[0] & /*_color_map*/
      8192 && (c._color_map = /*_color_map*/
      r[13]), u[0] & /*info*/
      4 && (c.info = /*info*/
      r[2]), u[0] & /*label*/
      1 | u[1] & /*$$scope*/
      512 && (c.$$scope = { dirty: u, ctx: r }), t.$set(c);
      const m = {};
      u[0] & /*show_copy_button*/
      128 && (m.show_copy_button = /*show_copy_button*/
      r[7]), u[0] & /*show_remove_tags_button, tags_removed*/
      16640 && (m.show_remove_tags_button = /*show_remove_tags_button*/
      r[8] && !/*tags_removed*/
      r[14]), u[0] & /*tagged_text*/
      32768 && (m.value = /*tagged_text*/
      r[15]), i.$set(m), a === (a = f(r)) && _ ? _.p(r, u) : (_.d(1), _ = a(r), _ && (_.c(), _.m(e, null))), (!s || u[0] & /*container*/
      64) && Ft(
        e,
        "container",
        /*container*/
        r[6]
      );
    },
    i(r) {
      s || (Ht(t.$$.fragment, r), Ht(i.$$.fragment, r), s = !0);
    },
    o(r) {
      Mt(t.$$.fragment, r), Mt(i.$$.fragment, r), s = !1;
    },
    d(r) {
      r && Pe(e), Tt(t), Tt(i), _.d();
    }
  };
}
function ri(l, e, t) {
  const n = typeof document < "u";
  let { value: i = [] } = e, { value_is_output: o = !1 } = e, { label: s } = e, { legend_label: f } = e, { info: a = void 0 } = e, { show_label: _ = !0 } = e, { show_legend: r = !1 } = e, { show_legend_label: u = !1 } = e, { container: c = !0 } = e, { color_map: m = {} } = e, { show_copy_button: k = !1 } = e, { show_remove_tags_button: L = !1 } = e, { disabled: T } = e, S, y = "", d = "", C, j = !m || Object.keys(m).length === 0 ? {} : m, h = {}, Z = !1, J = "";
  function E() {
    for (let g in j)
      i.map(([M, F]) => F).includes(g) || delete j[g];
    if (i.length > 0) {
      for (let [g, M] of i)
        if (M !== null && !(M in j)) {
          let F = Xn(Object.keys(j).length);
          j[M] = F;
        }
    }
    t(13, h = Yn(j, n, C));
  }
  function O(g) {
    i.length > 0 && g && (t(11, y = i.map(([M, F]) => M).join("")), t(12, d = i.map(([M, F]) => F !== null ? `<mark class="hl ${F}" style="background-color:${h[F].secondary}">${M}</mark>` : M).join("")), t(15, J = i.map(([M, F]) => F !== null ? `<${F}>${M}</${F}>` : M).join("")));
  }
  const R = oi();
  ni(() => {
    S && S.offsetHeight + S.scrollTop > S.scrollHeight - 100;
  });
  function ae() {
    D(), A(), R("change", i), o || R("input", i);
  }
  ii(() => {
    E(), O(o), t(19, o = !1);
  });
  function A() {
    let g = [], M = "", F = null, ee = !1, be = "", we = d.replace(/&nbsp;|&amp;|&lt;|&gt;/g, function(te) {
      return {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">"
      }[te];
    });
    for (let te = 0; te < we.length; te++) {
      let Q = we[te];
      if (Q === "<")
        ee = !0, M && g.push([M, F]), M = "", F = null;
      else if (Q === ">") {
        if (ee = !1, be.slice(0, 4) === "mark") {
          let Ne = /class="hl ([^"]+)"/.exec(be);
          F = Ne ? Ne[1] : null;
        }
        be = "";
      } else
        ee ? be += Q : M += Q;
    }
    M && g.push([M, F]), t(18, i = g);
  }
  function K() {
    t(12, d = y), ae(), t(14, Z = !0), R("clear");
  }
  function D() {
    const g = window.getSelection(), M = g.anchorOffset;
    if (g.rangeCount > 0) {
      var F = g.getRangeAt(0).commonAncestorContainer.parentElement;
      if (F && F.tagName.toLowerCase() === "mark") {
        const Ne = F.textContent;
        var ee = F.parentElement, be = document.createTextNode(Ne);
        ee.replaceChild(be, F), t(12, d = ee.innerHTML);
        var we = document.createRange(), te = window.getSelection();
        const kl = M + Jn(ee);
        var Q = Kn(ee, kl);
        we.setStart(Q.node, Q.offset), we.setEnd(Q.node, Q.offset), te.removeAllRanges(), te.addRange(we);
      }
    }
  }
  function me(g) {
    je.call(this, l, g);
  }
  function Le(g) {
    je.call(this, l, g);
  }
  function ge(g) {
    je.call(this, l, g);
  }
  function b(g) {
    je.call(this, l, g);
  }
  function he(g) {
    je.call(this, l, g);
  }
  function Oe(g) {
    qt[g ? "unshift" : "push"](() => {
      S = g, t(10, S);
    });
  }
  function Ae() {
    y = this.textContent, d = this.innerHTML, t(11, y), t(12, d);
  }
  function w(g) {
    qt[g ? "unshift" : "push"](() => {
      S = g, t(10, S);
    });
  }
  function pl() {
    y = this.textContent, d = this.innerHTML, t(11, y), t(12, d);
  }
  return l.$$set = (g) => {
    "value" in g && t(18, i = g.value), "value_is_output" in g && t(19, o = g.value_is_output), "label" in g && t(0, s = g.label), "legend_label" in g && t(1, f = g.legend_label), "info" in g && t(2, a = g.info), "show_label" in g && t(3, _ = g.show_label), "show_legend" in g && t(4, r = g.show_legend), "show_legend_label" in g && t(5, u = g.show_legend_label), "container" in g && t(6, c = g.container), "color_map" in g && t(20, m = g.color_map), "show_copy_button" in g && t(7, k = g.show_copy_button), "show_remove_tags_button" in g && t(8, L = g.show_remove_tags_button), "disabled" in g && t(9, T = g.disabled);
  }, E(), O(!0), [
    s,
    f,
    a,
    _,
    r,
    u,
    c,
    k,
    L,
    T,
    S,
    y,
    d,
    h,
    Z,
    J,
    ae,
    K,
    i,
    o,
    m,
    me,
    Le,
    ge,
    b,
    he,
    Oe,
    Ae,
    w,
    pl
  ];
}
class ui extends Qn {
  constructor(e) {
    super(), xn(
      this,
      e,
      ri,
      ai,
      ei,
      {
        value: 18,
        value_is_output: 19,
        label: 0,
        legend_label: 1,
        info: 2,
        show_label: 3,
        show_legend: 4,
        show_legend_label: 5,
        container: 6,
        color_map: 20,
        show_copy_button: 7,
        show_remove_tags_button: 8,
        disabled: 9
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: ci,
  assign: di,
  create_slot: mi,
  detach: gi,
  element: hi,
  get_all_dirty_from_scope: bi,
  get_slot_changes: wi,
  get_spread_update: vi,
  init: pi,
  insert: ki,
  safe_not_equal: yi,
  set_dynamic_element_data: Nt,
  set_style: z,
  toggle_class: ne,
  transition_in: gl,
  transition_out: hl,
  update_slot_base: Ci
} = window.__gradio__svelte__internal;
function qi(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), o = mi(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let s = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-1t38q2d"
    }
  ], f = {};
  for (let a = 0; a < s.length; a += 1)
    f = di(f, s[a]);
  return {
    c() {
      e = hi(
        /*tag*/
        l[14]
      ), o && o.c(), Nt(
        /*tag*/
        l[14]
      )(e, f), ne(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), ne(
        e,
        "padded",
        /*padding*/
        l[6]
      ), ne(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), ne(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), z(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), z(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), z(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), z(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), z(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), z(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), z(e, "border-width", "var(--block-border-width)");
    },
    m(a, _) {
      ki(a, e, _), o && o.m(e, null), n = !0;
    },
    p(a, _) {
      o && o.p && (!n || _ & /*$$scope*/
      131072) && Ci(
        o,
        i,
        a,
        /*$$scope*/
        a[17],
        n ? wi(
          i,
          /*$$scope*/
          a[17],
          _,
          null
        ) : bi(
          /*$$scope*/
          a[17]
        ),
        null
      ), Nt(
        /*tag*/
        a[14]
      )(e, f = vi(s, [
        (!n || _ & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          a[7]
        ) },
        (!n || _ & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          a[2]
        ) },
        (!n || _ & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        a[3].join(" ") + " svelte-1t38q2d")) && { class: t }
      ])), ne(
        e,
        "hidden",
        /*visible*/
        a[10] === !1
      ), ne(
        e,
        "padded",
        /*padding*/
        a[6]
      ), ne(
        e,
        "border_focus",
        /*border_mode*/
        a[5] === "focus"
      ), ne(e, "hide-container", !/*explicit_call*/
      a[8] && !/*container*/
      a[9]), _ & /*height*/
      1 && z(
        e,
        "height",
        /*get_dimension*/
        a[15](
          /*height*/
          a[0]
        )
      ), _ & /*width*/
      2 && z(e, "width", typeof /*width*/
      a[1] == "number" ? `calc(min(${/*width*/
      a[1]}px, 100%))` : (
        /*get_dimension*/
        a[15](
          /*width*/
          a[1]
        )
      )), _ & /*variant*/
      16 && z(
        e,
        "border-style",
        /*variant*/
        a[4]
      ), _ & /*allow_overflow*/
      2048 && z(
        e,
        "overflow",
        /*allow_overflow*/
        a[11] ? "visible" : "hidden"
      ), _ & /*scale*/
      4096 && z(
        e,
        "flex-grow",
        /*scale*/
        a[12]
      ), _ & /*min_width*/
      8192 && z(e, "min-width", `calc(min(${/*min_width*/
      a[13]}px, 100%))`);
    },
    i(a) {
      n || (gl(o, a), n = !0);
    },
    o(a) {
      hl(o, a), n = !1;
    },
    d(a) {
      a && gi(e), o && o.d(a);
    }
  };
}
function Si(l) {
  let e, t = (
    /*tag*/
    l[14] && qi(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (gl(t, n), e = !0);
    },
    o(n) {
      hl(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function Ti(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: o = void 0 } = e, { width: s = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: a = [] } = e, { variant: _ = "solid" } = e, { border_mode: r = "base" } = e, { padding: u = !0 } = e, { type: c = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: k = !1 } = e, { container: L = !0 } = e, { visible: T = !0 } = e, { allow_overflow: S = !0 } = e, { scale: y = null } = e, { min_width: d = 0 } = e, C = c === "fieldset" ? "fieldset" : "div";
  const j = (h) => {
    if (h !== void 0) {
      if (typeof h == "number")
        return h + "px";
      if (typeof h == "string")
        return h;
    }
  };
  return l.$$set = (h) => {
    "height" in h && t(0, o = h.height), "width" in h && t(1, s = h.width), "elem_id" in h && t(2, f = h.elem_id), "elem_classes" in h && t(3, a = h.elem_classes), "variant" in h && t(4, _ = h.variant), "border_mode" in h && t(5, r = h.border_mode), "padding" in h && t(6, u = h.padding), "type" in h && t(16, c = h.type), "test_id" in h && t(7, m = h.test_id), "explicit_call" in h && t(8, k = h.explicit_call), "container" in h && t(9, L = h.container), "visible" in h && t(10, T = h.visible), "allow_overflow" in h && t(11, S = h.allow_overflow), "scale" in h && t(12, y = h.scale), "min_width" in h && t(13, d = h.min_width), "$$scope" in h && t(17, i = h.$$scope);
  }, [
    o,
    s,
    f,
    a,
    _,
    r,
    u,
    m,
    k,
    L,
    T,
    S,
    y,
    d,
    C,
    j,
    c,
    i,
    n
  ];
}
class Li extends ci {
  constructor(e) {
    super(), pi(this, e, Ti, Si, yi, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
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
function ke(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
const {
  SvelteComponent: ji,
  append: W,
  attr: q,
  component_subscribe: Vt,
  detach: Fi,
  element: Hi,
  init: Mi,
  insert: Ni,
  noop: zt,
  safe_not_equal: Vi,
  set_style: ze,
  svg_element: I,
  toggle_class: Et
} = window.__gradio__svelte__internal, { onMount: zi } = window.__gradio__svelte__internal;
function Ei(l) {
  let e, t, n, i, o, s, f, a, _, r, u, c;
  return {
    c() {
      e = Hi("div"), t = I("svg"), n = I("g"), i = I("path"), o = I("path"), s = I("path"), f = I("path"), a = I("g"), _ = I("path"), r = I("path"), u = I("path"), c = I("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(o, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(o, "fill", "#FF7C00"), q(o, "class", "svelte-43sxxs"), q(s, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(s, "fill", "#FF7C00"), q(s, "fill-opacity", "0.4"), q(s, "class", "svelte-43sxxs"), q(f, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(f, "fill", "#FF7C00"), q(f, "class", "svelte-43sxxs"), ze(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(_, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(_, "fill", "#FF7C00"), q(_, "fill-opacity", "0.4"), q(_, "class", "svelte-43sxxs"), q(r, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(r, "fill", "#FF7C00"), q(r, "class", "svelte-43sxxs"), q(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(u, "fill", "#FF7C00"), q(u, "fill-opacity", "0.4"), q(u, "class", "svelte-43sxxs"), q(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), ze(a, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Et(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, k) {
      Ni(m, e, k), W(e, t), W(t, n), W(n, i), W(n, o), W(n, s), W(n, f), W(t, a), W(a, _), W(a, r), W(a, u), W(a, c);
    },
    p(m, [k]) {
      k & /*$top*/
      2 && ze(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), k & /*$bottom*/
      4 && ze(a, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), k & /*margin*/
      1 && Et(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: zt,
    o: zt,
    d(m) {
      m && Fi(e);
    }
  };
}
function Ri(l, e, t) {
  let n, i, { margin: o = !0 } = e;
  const s = at([0, 0]);
  Vt(l, s, (c) => t(1, n = c));
  const f = at([0, 0]);
  Vt(l, f, (c) => t(2, i = c));
  let a;
  async function _() {
    await Promise.all([s.set([125, 140]), f.set([-125, -140])]), await Promise.all([s.set([-125, 140]), f.set([125, -140])]), await Promise.all([s.set([-125, 0]), f.set([125, -0])]), await Promise.all([s.set([125, 0]), f.set([-125, 0])]);
  }
  async function r() {
    await _(), a || r();
  }
  async function u() {
    await Promise.all([s.set([125, 0]), f.set([-125, 0])]), r();
  }
  return zi(() => (u(), () => a = !0)), l.$$set = (c) => {
    "margin" in c && t(0, o = c.margin);
  }, [o, n, i, s, f];
}
class Di extends ji {
  constructor(e) {
    super(), Mi(this, e, Ri, Ei, Vi, { margin: 0 });
  }
}
const {
  SvelteComponent: Bi,
  append: ce,
  attr: Y,
  binding_callbacks: Rt,
  check_outros: bl,
  create_component: Pi,
  create_slot: Zi,
  destroy_component: Oi,
  destroy_each: wl,
  detach: v,
  element: $,
  empty: Te,
  ensure_array_like: Be,
  get_all_dirty_from_scope: Ai,
  get_slot_changes: Wi,
  group_outros: vl,
  init: Ii,
  insert: p,
  mount_component: Ui,
  noop: Ge,
  safe_not_equal: Xi,
  set_data: P,
  set_style: oe,
  space: G,
  text: H,
  toggle_class: B,
  transition_in: qe,
  transition_out: Se,
  update_slot_base: Yi
} = window.__gradio__svelte__internal, { tick: Gi } = window.__gradio__svelte__internal, { onDestroy: Ji } = window.__gradio__svelte__internal, Ki = (l) => ({}), Dt = (l) => ({});
function Bt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n[40] = t, n;
}
function Pt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n;
}
function Qi(l) {
  let e, t = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, o;
  const s = (
    /*#slots*/
    l[29].error
  ), f = Zi(
    s,
    l,
    /*$$scope*/
    l[28],
    Dt
  );
  return {
    c() {
      e = $("span"), n = H(t), i = G(), f && f.c(), Y(e, "class", "error svelte-1txqlrd");
    },
    m(a, _) {
      p(a, e, _), ce(e, n), p(a, i, _), f && f.m(a, _), o = !0;
    },
    p(a, _) {
      (!o || _[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      a[1]("common.error") + "") && P(n, t), f && f.p && (!o || _[0] & /*$$scope*/
      268435456) && Yi(
        f,
        s,
        a,
        /*$$scope*/
        a[28],
        o ? Wi(
          s,
          /*$$scope*/
          a[28],
          _,
          Ki
        ) : Ai(
          /*$$scope*/
          a[28]
        ),
        Dt
      );
    },
    i(a) {
      o || (qe(f, a), o = !0);
    },
    o(a) {
      Se(f, a), o = !1;
    },
    d(a) {
      a && (v(e), v(i)), f && f.d(a);
    }
  };
}
function xi(l) {
  let e, t, n, i, o, s, f, a, _, r = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Zt(l)
  );
  function u(d, C) {
    if (
      /*progress*/
      d[7]
    )
      return to;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return eo;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return $i;
  }
  let c = u(l), m = c && c(l), k = (
    /*timer*/
    l[5] && Wt(l)
  );
  const L = [oo, io], T = [];
  function S(d, C) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(o = S(l)) && (s = T[o] = L[o](l));
  let y = !/*timer*/
  l[5] && Kt(l);
  return {
    c() {
      r && r.c(), e = G(), t = $("div"), m && m.c(), n = G(), k && k.c(), i = G(), s && s.c(), f = G(), y && y.c(), a = Te(), Y(t, "class", "progress-text svelte-1txqlrd"), B(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), B(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(d, C) {
      r && r.m(d, C), p(d, e, C), p(d, t, C), m && m.m(t, null), ce(t, n), k && k.m(t, null), p(d, i, C), ~o && T[o].m(d, C), p(d, f, C), y && y.m(d, C), p(d, a, C), _ = !0;
    },
    p(d, C) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? r ? r.p(d, C) : (r = Zt(d), r.c(), r.m(e.parentNode, e)) : r && (r.d(1), r = null), c === (c = u(d)) && m ? m.p(d, C) : (m && m.d(1), m = c && c(d), m && (m.c(), m.m(t, n))), /*timer*/
      d[5] ? k ? k.p(d, C) : (k = Wt(d), k.c(), k.m(t, null)) : k && (k.d(1), k = null), (!_ || C[0] & /*variant*/
      256) && B(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!_ || C[0] & /*variant*/
      256) && B(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let j = o;
      o = S(d), o === j ? ~o && T[o].p(d, C) : (s && (vl(), Se(T[j], 1, 1, () => {
        T[j] = null;
      }), bl()), ~o ? (s = T[o], s ? s.p(d, C) : (s = T[o] = L[o](d), s.c()), qe(s, 1), s.m(f.parentNode, f)) : s = null), /*timer*/
      d[5] ? y && (y.d(1), y = null) : y ? y.p(d, C) : (y = Kt(d), y.c(), y.m(a.parentNode, a));
    },
    i(d) {
      _ || (qe(s), _ = !0);
    },
    o(d) {
      Se(s), _ = !1;
    },
    d(d) {
      d && (v(e), v(t), v(i), v(f), v(a)), r && r.d(d), m && m.d(), k && k.d(), ~o && T[o].d(d), y && y.d(d);
    }
  };
}
function Zt(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = $("div"), Y(e, "class", "eta-bar svelte-1txqlrd"), oe(e, "transform", t);
    },
    m(n, i) {
      p(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && oe(e, "transform", t);
    },
    d(n) {
      n && v(e);
    }
  };
}
function $i(l) {
  let e;
  return {
    c() {
      e = H("processing |");
    },
    m(t, n) {
      p(t, e, n);
    },
    p: Ge,
    d(t) {
      t && v(e);
    }
  };
}
function eo(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, o, s;
  return {
    c() {
      e = H("queue: "), n = H(t), i = H("/"), o = H(
        /*queue_size*/
        l[3]
      ), s = H(" |");
    },
    m(f, a) {
      p(f, e, a), p(f, n, a), p(f, i, a), p(f, o, a), p(f, s, a);
    },
    p(f, a) {
      a[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      f[2] + 1 + "") && P(n, t), a[0] & /*queue_size*/
      8 && P(
        o,
        /*queue_size*/
        f[3]
      );
    },
    d(f) {
      f && (v(e), v(n), v(i), v(o), v(s));
    }
  };
}
function to(l) {
  let e, t = Be(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = At(Pt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Te();
    },
    m(i, o) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, o);
      p(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress*/
      128) {
        t = Be(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const f = Pt(i, t, s);
          n[s] ? n[s].p(f, o) : (n[s] = At(f), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && v(e), wl(n, i);
    }
  };
}
function Ot(l) {
  let e, t = (
    /*p*/
    l[38].unit + ""
  ), n, i, o = " ", s;
  function f(r, u) {
    return (
      /*p*/
      r[38].length != null ? no : lo
    );
  }
  let a = f(l), _ = a(l);
  return {
    c() {
      _.c(), e = G(), n = H(t), i = H(" | "), s = H(o);
    },
    m(r, u) {
      _.m(r, u), p(r, e, u), p(r, n, u), p(r, i, u), p(r, s, u);
    },
    p(r, u) {
      a === (a = f(r)) && _ ? _.p(r, u) : (_.d(1), _ = a(r), _ && (_.c(), _.m(e.parentNode, e))), u[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[38].unit + "") && P(n, t);
    },
    d(r) {
      r && (v(e), v(n), v(i), v(s)), _.d(r);
    }
  };
}
function lo(l) {
  let e = ke(
    /*p*/
    l[38].index || 0
  ) + "", t;
  return {
    c() {
      t = H(e);
    },
    m(n, i) {
      p(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = ke(
        /*p*/
        n[38].index || 0
      ) + "") && P(t, e);
    },
    d(n) {
      n && v(t);
    }
  };
}
function no(l) {
  let e = ke(
    /*p*/
    l[38].index || 0
  ) + "", t, n, i = ke(
    /*p*/
    l[38].length
  ) + "", o;
  return {
    c() {
      t = H(e), n = H("/"), o = H(i);
    },
    m(s, f) {
      p(s, t, f), p(s, n, f), p(s, o, f);
    },
    p(s, f) {
      f[0] & /*progress*/
      128 && e !== (e = ke(
        /*p*/
        s[38].index || 0
      ) + "") && P(t, e), f[0] & /*progress*/
      128 && i !== (i = ke(
        /*p*/
        s[38].length
      ) + "") && P(o, i);
    },
    d(s) {
      s && (v(t), v(n), v(o));
    }
  };
}
function At(l) {
  let e, t = (
    /*p*/
    l[38].index != null && Ot(l)
  );
  return {
    c() {
      t && t.c(), e = Te();
    },
    m(n, i) {
      t && t.m(n, i), p(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? t ? t.p(n, i) : (t = Ot(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && v(e), t && t.d(n);
    }
  };
}
function Wt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = H(
        /*formatted_timer*/
        l[20]
      ), n = H(t), i = H("s");
    },
    m(o, s) {
      p(o, e, s), p(o, n, s), p(o, i, s);
    },
    p(o, s) {
      s[0] & /*formatted_timer*/
      1048576 && P(
        e,
        /*formatted_timer*/
        o[20]
      ), s[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      o[0] ? `/${/*formatted_eta*/
      o[19]}` : "") && P(n, t);
    },
    d(o) {
      o && (v(e), v(n), v(i));
    }
  };
}
function io(l) {
  let e, t;
  return e = new Di({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      Pi(e.$$.fragment);
    },
    m(n, i) {
      Ui(e, n, i), t = !0;
    },
    p(n, i) {
      const o = {};
      i[0] & /*variant*/
      256 && (o.margin = /*variant*/
      n[8] === "default"), e.$set(o);
    },
    i(n) {
      t || (qe(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Se(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Oi(e, n);
    }
  };
}
function oo(l) {
  let e, t, n, i, o, s = `${/*last_progress_level*/
  l[15] * 100}%`, f = (
    /*progress*/
    l[7] != null && It(l)
  );
  return {
    c() {
      e = $("div"), t = $("div"), f && f.c(), n = G(), i = $("div"), o = $("div"), Y(t, "class", "progress-level-inner svelte-1txqlrd"), Y(o, "class", "progress-bar svelte-1txqlrd"), oe(o, "width", s), Y(i, "class", "progress-bar-wrap svelte-1txqlrd"), Y(e, "class", "progress-level svelte-1txqlrd");
    },
    m(a, _) {
      p(a, e, _), ce(e, t), f && f.m(t, null), ce(e, n), ce(e, i), ce(i, o), l[30](o);
    },
    p(a, _) {
      /*progress*/
      a[7] != null ? f ? f.p(a, _) : (f = It(a), f.c(), f.m(t, null)) : f && (f.d(1), f = null), _[0] & /*last_progress_level*/
      32768 && s !== (s = `${/*last_progress_level*/
      a[15] * 100}%`) && oe(o, "width", s);
    },
    i: Ge,
    o: Ge,
    d(a) {
      a && v(e), f && f.d(), l[30](null);
    }
  };
}
function It(l) {
  let e, t = Be(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Jt(Bt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Te();
    },
    m(i, o) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, o);
      p(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress_level, progress*/
      16512) {
        t = Be(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const f = Bt(i, t, s);
          n[s] ? n[s].p(f, o) : (n[s] = Jt(f), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && v(e), wl(n, i);
    }
  };
}
function Ut(l) {
  let e, t, n, i, o = (
    /*i*/
    l[40] !== 0 && so()
  ), s = (
    /*p*/
    l[38].desc != null && Xt(l)
  ), f = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && Yt()
  ), a = (
    /*progress_level*/
    l[14] != null && Gt(l)
  );
  return {
    c() {
      o && o.c(), e = G(), s && s.c(), t = G(), f && f.c(), n = G(), a && a.c(), i = Te();
    },
    m(_, r) {
      o && o.m(_, r), p(_, e, r), s && s.m(_, r), p(_, t, r), f && f.m(_, r), p(_, n, r), a && a.m(_, r), p(_, i, r);
    },
    p(_, r) {
      /*p*/
      _[38].desc != null ? s ? s.p(_, r) : (s = Xt(_), s.c(), s.m(t.parentNode, t)) : s && (s.d(1), s = null), /*p*/
      _[38].desc != null && /*progress_level*/
      _[14] && /*progress_level*/
      _[14][
        /*i*/
        _[40]
      ] != null ? f || (f = Yt(), f.c(), f.m(n.parentNode, n)) : f && (f.d(1), f = null), /*progress_level*/
      _[14] != null ? a ? a.p(_, r) : (a = Gt(_), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null);
    },
    d(_) {
      _ && (v(e), v(t), v(n), v(i)), o && o.d(_), s && s.d(_), f && f.d(_), a && a.d(_);
    }
  };
}
function so(l) {
  let e;
  return {
    c() {
      e = H(" /");
    },
    m(t, n) {
      p(t, e, n);
    },
    d(t) {
      t && v(e);
    }
  };
}
function Xt(l) {
  let e = (
    /*p*/
    l[38].desc + ""
  ), t;
  return {
    c() {
      t = H(e);
    },
    m(n, i) {
      p(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[38].desc + "") && P(t, e);
    },
    d(n) {
      n && v(t);
    }
  };
}
function Yt(l) {
  let e;
  return {
    c() {
      e = H("-");
    },
    m(t, n) {
      p(t, e, n);
    },
    d(t) {
      t && v(e);
    }
  };
}
function Gt(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[40]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = H(e), n = H("%");
    },
    m(i, o) {
      p(i, t, o), p(i, n, o);
    },
    p(i, o) {
      o[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && P(t, e);
    },
    d(i) {
      i && (v(t), v(n));
    }
  };
}
function Jt(l) {
  let e, t = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && Ut(l)
  );
  return {
    c() {
      t && t.c(), e = Te();
    },
    m(n, i) {
      t && t.m(n, i), p(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[40]
      ] != null ? t ? t.p(n, i) : (t = Ut(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && v(e), t && t.d(n);
    }
  };
}
function Kt(l) {
  let e, t;
  return {
    c() {
      e = $("p"), t = H(
        /*loading_text*/
        l[9]
      ), Y(e, "class", "loading svelte-1txqlrd");
    },
    m(n, i) {
      p(n, e, i), ce(e, t);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && P(
        t,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && v(e);
    }
  };
}
function fo(l) {
  let e, t, n, i, o;
  const s = [xi, Qi], f = [];
  function a(_, r) {
    return (
      /*status*/
      _[4] === "pending" ? 0 : (
        /*status*/
        _[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = a(l)) && (n = f[t] = s[t](l)), {
    c() {
      e = $("div"), n && n.c(), Y(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1txqlrd"), B(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), B(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), B(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), B(
        e,
        "border",
        /*border*/
        l[12]
      ), oe(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), oe(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(_, r) {
      p(_, e, r), ~t && f[t].m(e, null), l[31](e), o = !0;
    },
    p(_, r) {
      let u = t;
      t = a(_), t === u ? ~t && f[t].p(_, r) : (n && (vl(), Se(f[u], 1, 1, () => {
        f[u] = null;
      }), bl()), ~t ? (n = f[t], n ? n.p(_, r) : (n = f[t] = s[t](_), n.c()), qe(n, 1), n.m(e, null)) : n = null), (!o || r[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      _[8] + " " + /*show_progress*/
      _[6] + " svelte-1txqlrd")) && Y(e, "class", i), (!o || r[0] & /*variant, show_progress, status, show_progress*/
      336) && B(e, "hide", !/*status*/
      _[4] || /*status*/
      _[4] === "complete" || /*show_progress*/
      _[6] === "hidden"), (!o || r[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && B(
        e,
        "translucent",
        /*variant*/
        _[8] === "center" && /*status*/
        (_[4] === "pending" || /*status*/
        _[4] === "error") || /*translucent*/
        _[11] || /*show_progress*/
        _[6] === "minimal"
      ), (!o || r[0] & /*variant, show_progress, status*/
      336) && B(
        e,
        "generating",
        /*status*/
        _[4] === "generating"
      ), (!o || r[0] & /*variant, show_progress, border*/
      4416) && B(
        e,
        "border",
        /*border*/
        _[12]
      ), r[0] & /*absolute*/
      1024 && oe(
        e,
        "position",
        /*absolute*/
        _[10] ? "absolute" : "static"
      ), r[0] & /*absolute*/
      1024 && oe(
        e,
        "padding",
        /*absolute*/
        _[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(_) {
      o || (qe(n), o = !0);
    },
    o(_) {
      Se(n), o = !1;
    },
    d(_) {
      _ && v(e), ~t && f[t].d(), l[31](null);
    }
  };
}
let Ee = [], Xe = !1;
async function _o(l, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (Ee.push(l), !Xe)
      Xe = !0;
    else
      return;
    await Gi(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let n = 0; n < Ee.length; n++) {
        const o = Ee[n].getBoundingClientRect();
        (n === 0 || o.top + window.scrollY <= t[0]) && (t[0] = o.top + window.scrollY, t[1] = n);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), Xe = !1, Ee = [];
    });
  }
}
function ao(l, e, t) {
  let n, { $$slots: i = {}, $$scope: o } = e, { i18n: s } = e, { eta: f = null } = e, { queue_position: a } = e, { queue_size: _ } = e, { status: r } = e, { scroll_to_output: u = !1 } = e, { timer: c = !0 } = e, { show_progress: m = "full" } = e, { message: k = null } = e, { progress: L = null } = e, { variant: T = "default" } = e, { loading_text: S = "Loading..." } = e, { absolute: y = !0 } = e, { translucent: d = !1 } = e, { border: C = !1 } = e, { autoscroll: j } = e, h, Z = !1, J = 0, E = 0, O = null, R = null, ae = 0, A = null, K, D = null, me = !0;
  const Le = () => {
    t(0, f = t(26, O = t(19, he = null))), t(24, J = performance.now()), t(25, E = 0), Z = !0, ge();
  };
  function ge() {
    requestAnimationFrame(() => {
      t(25, E = (performance.now() - J) / 1e3), Z && ge();
    });
  }
  function b() {
    t(25, E = 0), t(0, f = t(26, O = t(19, he = null))), Z && (Z = !1);
  }
  Ji(() => {
    Z && b();
  });
  let he = null;
  function Oe(w) {
    Rt[w ? "unshift" : "push"](() => {
      D = w, t(16, D), t(7, L), t(14, A), t(15, K);
    });
  }
  function Ae(w) {
    Rt[w ? "unshift" : "push"](() => {
      h = w, t(13, h);
    });
  }
  return l.$$set = (w) => {
    "i18n" in w && t(1, s = w.i18n), "eta" in w && t(0, f = w.eta), "queue_position" in w && t(2, a = w.queue_position), "queue_size" in w && t(3, _ = w.queue_size), "status" in w && t(4, r = w.status), "scroll_to_output" in w && t(21, u = w.scroll_to_output), "timer" in w && t(5, c = w.timer), "show_progress" in w && t(6, m = w.show_progress), "message" in w && t(22, k = w.message), "progress" in w && t(7, L = w.progress), "variant" in w && t(8, T = w.variant), "loading_text" in w && t(9, S = w.loading_text), "absolute" in w && t(10, y = w.absolute), "translucent" in w && t(11, d = w.translucent), "border" in w && t(12, C = w.border), "autoscroll" in w && t(23, j = w.autoscroll), "$$scope" in w && t(28, o = w.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (f === null && t(0, f = O), f != null && O !== f && (t(27, R = (performance.now() - J) / 1e3 + f), t(19, he = R.toFixed(1)), t(26, O = f))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && t(17, ae = R === null || R <= 0 || !E ? null : Math.min(E / R, 1)), l.$$.dirty[0] & /*progress*/
    128 && L != null && t(18, me = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (L != null ? t(14, A = L.map((w) => {
      if (w.index != null && w.length != null)
        return w.index / w.length;
      if (w.progress != null)
        return w.progress;
    })) : t(14, A = null), A ? (t(15, K = A[A.length - 1]), D && (K === 0 ? t(16, D.style.transition = "0", D) : t(16, D.style.transition = "150ms", D))) : t(15, K = void 0)), l.$$.dirty[0] & /*status*/
    16 && (r === "pending" ? Le() : b()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && h && u && (r === "pending" || r === "complete") && _o(h, j), l.$$.dirty[0] & /*status, message*/
    4194320, l.$$.dirty[0] & /*timer_diff*/
    33554432 && t(20, n = E.toFixed(1));
  }, [
    f,
    s,
    a,
    _,
    r,
    c,
    m,
    L,
    T,
    S,
    y,
    d,
    C,
    h,
    A,
    K,
    D,
    ae,
    me,
    he,
    n,
    u,
    k,
    j,
    J,
    E,
    O,
    R,
    o,
    i,
    Oe,
    Ae
  ];
}
class ro extends Bi {
  constructor(e) {
    super(), Ii(
      this,
      e,
      ao,
      fo,
      Xi,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 21,
        timer: 5,
        show_progress: 6,
        message: 22,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 23
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: uo,
  add_flush_callback: Qt,
  assign: co,
  bind: xt,
  binding_callbacks: $t,
  check_outros: mo,
  create_component: xe,
  destroy_component: $e,
  detach: go,
  flush: N,
  get_spread_object: ho,
  get_spread_update: bo,
  group_outros: wo,
  init: vo,
  insert: po,
  mount_component: et,
  safe_not_equal: ko,
  space: yo,
  transition_in: ye,
  transition_out: He
} = window.__gradio__svelte__internal;
function el(l) {
  let e, t;
  const n = [
    { autoscroll: (
      /*gradio*/
      l[3].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[3].i18n
    ) },
    /*loading_status*/
    l[18]
  ];
  let i = {};
  for (let o = 0; o < n.length; o += 1)
    i = co(i, n[o]);
  return e = new ro({ props: i }), {
    c() {
      xe(e.$$.fragment);
    },
    m(o, s) {
      et(e, o, s), t = !0;
    },
    p(o, s) {
      const f = s[0] & /*gradio, loading_status*/
      262152 ? bo(n, [
        s[0] & /*gradio*/
        8 && { autoscroll: (
          /*gradio*/
          o[3].autoscroll
        ) },
        s[0] & /*gradio*/
        8 && { i18n: (
          /*gradio*/
          o[3].i18n
        ) },
        s[0] & /*loading_status*/
        262144 && ho(
          /*loading_status*/
          o[18]
        )
      ]) : {};
      e.$set(f);
    },
    i(o) {
      t || (ye(e.$$.fragment, o), t = !0);
    },
    o(o) {
      He(e.$$.fragment, o), t = !1;
    },
    d(o) {
      $e(e, o);
    }
  };
}
function Co(l) {
  let e, t, n, i, o, s = (
    /*loading_status*/
    l[18] && el(l)
  );
  function f(r) {
    l[23](r);
  }
  function a(r) {
    l[24](r);
  }
  let _ = {
    label: (
      /*label*/
      l[4]
    ),
    info: (
      /*info*/
      l[6]
    ),
    show_label: (
      /*show_label*/
      l[10]
    ),
    show_legend: (
      /*show_legend*/
      l[11]
    ),
    show_legend_label: (
      /*show_legend_label*/
      l[12]
    ),
    legend_label: (
      /*legend_label*/
      l[5]
    ),
    color_map: (
      /*color_map*/
      l[1]
    ),
    show_copy_button: (
      /*show_copy_button*/
      l[16]
    ),
    show_remove_tags_button: (
      /*show_remove_tags_button*/
      l[17]
    ),
    container: (
      /*container*/
      l[13]
    ),
    disabled: !/*interactive*/
    l[19]
  };
  return (
    /*value*/
    l[0] !== void 0 && (_.value = /*value*/
    l[0]), /*value_is_output*/
    l[2] !== void 0 && (_.value_is_output = /*value_is_output*/
    l[2]), t = new ui({ props: _ }), $t.push(() => xt(t, "value", f)), $t.push(() => xt(t, "value_is_output", a)), t.$on(
      "change",
      /*change_handler*/
      l[25]
    ), t.$on(
      "input",
      /*input_handler*/
      l[26]
    ), t.$on(
      "submit",
      /*submit_handler*/
      l[27]
    ), t.$on(
      "blur",
      /*blur_handler*/
      l[28]
    ), t.$on(
      "select",
      /*select_handler*/
      l[29]
    ), t.$on(
      "focus",
      /*focus_handler*/
      l[30]
    ), t.$on(
      "clear",
      /*clear_handler*/
      l[31]
    ), {
      c() {
        s && s.c(), e = yo(), xe(t.$$.fragment);
      },
      m(r, u) {
        s && s.m(r, u), po(r, e, u), et(t, r, u), o = !0;
      },
      p(r, u) {
        /*loading_status*/
        r[18] ? s ? (s.p(r, u), u[0] & /*loading_status*/
        262144 && ye(s, 1)) : (s = el(r), s.c(), ye(s, 1), s.m(e.parentNode, e)) : s && (wo(), He(s, 1, 1, () => {
          s = null;
        }), mo());
        const c = {};
        u[0] & /*label*/
        16 && (c.label = /*label*/
        r[4]), u[0] & /*info*/
        64 && (c.info = /*info*/
        r[6]), u[0] & /*show_label*/
        1024 && (c.show_label = /*show_label*/
        r[10]), u[0] & /*show_legend*/
        2048 && (c.show_legend = /*show_legend*/
        r[11]), u[0] & /*show_legend_label*/
        4096 && (c.show_legend_label = /*show_legend_label*/
        r[12]), u[0] & /*legend_label*/
        32 && (c.legend_label = /*legend_label*/
        r[5]), u[0] & /*color_map*/
        2 && (c.color_map = /*color_map*/
        r[1]), u[0] & /*show_copy_button*/
        65536 && (c.show_copy_button = /*show_copy_button*/
        r[16]), u[0] & /*show_remove_tags_button*/
        131072 && (c.show_remove_tags_button = /*show_remove_tags_button*/
        r[17]), u[0] & /*container*/
        8192 && (c.container = /*container*/
        r[13]), u[0] & /*interactive*/
        524288 && (c.disabled = !/*interactive*/
        r[19]), !n && u[0] & /*value*/
        1 && (n = !0, c.value = /*value*/
        r[0], Qt(() => n = !1)), !i && u[0] & /*value_is_output*/
        4 && (i = !0, c.value_is_output = /*value_is_output*/
        r[2], Qt(() => i = !1)), t.$set(c);
      },
      i(r) {
        o || (ye(s), ye(t.$$.fragment, r), o = !0);
      },
      o(r) {
        He(s), He(t.$$.fragment, r), o = !1;
      },
      d(r) {
        r && go(e), s && s.d(r), $e(t, r);
      }
    }
  );
}
function qo(l) {
  let e, t;
  return e = new Li({
    props: {
      visible: (
        /*visible*/
        l[9]
      ),
      elem_id: (
        /*elem_id*/
        l[7]
      ),
      elem_classes: (
        /*elem_classes*/
        l[8]
      ),
      scale: (
        /*scale*/
        l[14]
      ),
      min_width: (
        /*min_width*/
        l[15]
      ),
      allow_overflow: !1,
      padding: (
        /*container*/
        l[13]
      ),
      $$slots: { default: [Co] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      xe(e.$$.fragment);
    },
    m(n, i) {
      et(e, n, i), t = !0;
    },
    p(n, i) {
      const o = {};
      i[0] & /*visible*/
      512 && (o.visible = /*visible*/
      n[9]), i[0] & /*elem_id*/
      128 && (o.elem_id = /*elem_id*/
      n[7]), i[0] & /*elem_classes*/
      256 && (o.elem_classes = /*elem_classes*/
      n[8]), i[0] & /*scale*/
      16384 && (o.scale = /*scale*/
      n[14]), i[0] & /*min_width*/
      32768 && (o.min_width = /*min_width*/
      n[15]), i[0] & /*container*/
      8192 && (o.padding = /*container*/
      n[13]), i[0] & /*label, info, show_label, show_legend, show_legend_label, legend_label, color_map, show_copy_button, show_remove_tags_button, container, interactive, value, value_is_output, gradio, loading_status*/
      998527 | i[1] & /*$$scope*/
      2 && (o.$$scope = { dirty: i, ctx: n }), e.$set(o);
    },
    i(n) {
      t || (ye(e.$$.fragment, n), t = !0);
    },
    o(n) {
      He(e.$$.fragment, n), t = !1;
    },
    d(n) {
      $e(e, n);
    }
  };
}
function So(l, e, t) {
  let { gradio: n } = e, { label: i = "Highlighted Textbox" } = e, { legend_label: o = "Highlights:" } = e, { info: s = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: a = [] } = e, { visible: _ = !0 } = e, { value: r } = e, { show_label: u } = e, { show_legend: c } = e, { show_legend_label: m } = e, { color_map: k = {} } = e, { container: L = !0 } = e, { scale: T = null } = e, { min_width: S = void 0 } = e, { show_copy_button: y = !1 } = e, { show_remove_tags_button: d = !1 } = e, { loading_status: C = void 0 } = e, { value_is_output: j = !1 } = e, { combine_adjacent: h = !1 } = e, { interactive: Z = !0 } = e;
  const J = !1, E = !0;
  function O(b) {
    r = b, t(0, r), t(20, h);
  }
  function R(b) {
    j = b, t(2, j);
  }
  const ae = () => n.dispatch("change"), A = () => n.dispatch("input"), K = () => n.dispatch("submit"), D = () => n.dispatch("blur"), me = (b) => n.dispatch("select", b.detail), Le = () => n.dispatch("focus"), ge = function() {
    console.log("test"), n.dispatch("clear");
  };
  return l.$$set = (b) => {
    "gradio" in b && t(3, n = b.gradio), "label" in b && t(4, i = b.label), "legend_label" in b && t(5, o = b.legend_label), "info" in b && t(6, s = b.info), "elem_id" in b && t(7, f = b.elem_id), "elem_classes" in b && t(8, a = b.elem_classes), "visible" in b && t(9, _ = b.visible), "value" in b && t(0, r = b.value), "show_label" in b && t(10, u = b.show_label), "show_legend" in b && t(11, c = b.show_legend), "show_legend_label" in b && t(12, m = b.show_legend_label), "color_map" in b && t(1, k = b.color_map), "container" in b && t(13, L = b.container), "scale" in b && t(14, T = b.scale), "min_width" in b && t(15, S = b.min_width), "show_copy_button" in b && t(16, y = b.show_copy_button), "show_remove_tags_button" in b && t(17, d = b.show_remove_tags_button), "loading_status" in b && t(18, C = b.loading_status), "value_is_output" in b && t(2, j = b.value_is_output), "combine_adjacent" in b && t(20, h = b.combine_adjacent), "interactive" in b && t(19, Z = b.interactive);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*color_map*/
    2 && !k && Object.keys(k).length && t(1, k), l.$$.dirty[0] & /*value, combine_adjacent*/
    1048577 && r && h && t(0, r = Gn(r, "equal"));
  }, [
    r,
    k,
    j,
    n,
    i,
    o,
    s,
    f,
    a,
    _,
    u,
    c,
    m,
    L,
    T,
    S,
    y,
    d,
    C,
    Z,
    h,
    J,
    E,
    O,
    R,
    ae,
    A,
    K,
    D,
    me,
    Le,
    ge
  ];
}
class To extends uo {
  constructor(e) {
    super(), vo(
      this,
      e,
      So,
      qo,
      ko,
      {
        gradio: 3,
        label: 4,
        legend_label: 5,
        info: 6,
        elem_id: 7,
        elem_classes: 8,
        visible: 9,
        value: 0,
        show_label: 10,
        show_legend: 11,
        show_legend_label: 12,
        color_map: 1,
        container: 13,
        scale: 14,
        min_width: 15,
        show_copy_button: 16,
        show_remove_tags_button: 17,
        loading_status: 18,
        value_is_output: 2,
        combine_adjacent: 20,
        interactive: 19,
        autofocus: 21,
        autoscroll: 22
      },
      null,
      [-1, -1]
    );
  }
  get gradio() {
    return this.$$.ctx[3];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), N();
  }
  get label() {
    return this.$$.ctx[4];
  }
  set label(e) {
    this.$$set({ label: e }), N();
  }
  get legend_label() {
    return this.$$.ctx[5];
  }
  set legend_label(e) {
    this.$$set({ legend_label: e }), N();
  }
  get info() {
    return this.$$.ctx[6];
  }
  set info(e) {
    this.$$set({ info: e }), N();
  }
  get elem_id() {
    return this.$$.ctx[7];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), N();
  }
  get elem_classes() {
    return this.$$.ctx[8];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), N();
  }
  get visible() {
    return this.$$.ctx[9];
  }
  set visible(e) {
    this.$$set({ visible: e }), N();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), N();
  }
  get show_label() {
    return this.$$.ctx[10];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), N();
  }
  get show_legend() {
    return this.$$.ctx[11];
  }
  set show_legend(e) {
    this.$$set({ show_legend: e }), N();
  }
  get show_legend_label() {
    return this.$$.ctx[12];
  }
  set show_legend_label(e) {
    this.$$set({ show_legend_label: e }), N();
  }
  get color_map() {
    return this.$$.ctx[1];
  }
  set color_map(e) {
    this.$$set({ color_map: e }), N();
  }
  get container() {
    return this.$$.ctx[13];
  }
  set container(e) {
    this.$$set({ container: e }), N();
  }
  get scale() {
    return this.$$.ctx[14];
  }
  set scale(e) {
    this.$$set({ scale: e }), N();
  }
  get min_width() {
    return this.$$.ctx[15];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), N();
  }
  get show_copy_button() {
    return this.$$.ctx[16];
  }
  set show_copy_button(e) {
    this.$$set({ show_copy_button: e }), N();
  }
  get show_remove_tags_button() {
    return this.$$.ctx[17];
  }
  set show_remove_tags_button(e) {
    this.$$set({ show_remove_tags_button: e }), N();
  }
  get loading_status() {
    return this.$$.ctx[18];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), N();
  }
  get value_is_output() {
    return this.$$.ctx[2];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), N();
  }
  get combine_adjacent() {
    return this.$$.ctx[20];
  }
  set combine_adjacent(e) {
    this.$$set({ combine_adjacent: e }), N();
  }
  get interactive() {
    return this.$$.ctx[19];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), N();
  }
  get autofocus() {
    return this.$$.ctx[21];
  }
  get autoscroll() {
    return this.$$.ctx[22];
  }
}
export {
  To as default
};
