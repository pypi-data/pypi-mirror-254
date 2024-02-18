(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6086],{59359:function(e,t,r){Promise.resolve().then(r.bind(r,93558))},93558:function(e,t,r){"use strict";r.r(t),r.d(t,{default:function(){return g}});var s=r(57437),o=r(2265),a=r(5925),i=r(24033),n=r(45987),l=r(23588),d=r(90262),u=r(68447),c=r(38110),p=r(61865),h=r(81698),m=r(92877);function b(e){var t,r,a,i,n;let{register:b,handleSubmit:f,setError:g,formState:{errors:v}}=(0,p.cI)({resolver:(0,c.F)(m.i2),mode:"onChange"}),{mutateAsync:y}=(0,l.D)({mutationFn:h.Z.user.first}),{onCreate:x,onAuthenticationError:k}=e,w=(0,o.useCallback)(e=>{let t=y(e,{onError:e=>{var t;let{status:r}=null!==(t=e.response)&&void 0!==t?t:{};switch(r){case 401:null==k||k(e);break;case 409:g("email",{message:"Email already exists"});break;default:g("username",{message:"Unknown error"})}}});null==x||x(t)},[g,k,y,x]);return(0,s.jsxs)("form",{className:"flex flex-col gap-1",onSubmit:f(w),children:[(0,s.jsx)(d.BZ,{label:"Username",name:"username",help:"This name will be used to identify you in the app.",error:null===(t=v.username)||void 0===t?void 0:t.message,children:(0,s.jsx)(d.II,{...b("username")})}),(0,s.jsx)(d.BZ,{label:"Name",name:"name",error:null===(r=v.name)||void 0===r?void 0:r.message,help:"Please provide your full name. This is especially helpful for sharing your annotations, ensuring correct attribution.",children:(0,s.jsx)(d.II,{...b("name")})}),(0,s.jsx)(d.BZ,{label:"Email",name:"email",error:null===(a=v.email)||void 0===a?void 0:a.message,help:"Provide a valid email address. While not displayed in the app, it helps others contact you regarding annotated data.",children:(0,s.jsx)(d.II,{type:"email",...b("email")})}),(0,s.jsx)(d.BZ,{label:"Password",name:"password",error:null===(i=v.password)||void 0===i?void 0:i.message,help:"Create a strong password with at least 8 characters, including one number and one letter.",children:(0,s.jsx)(d.II,{type:"password",...b("password")})}),(0,s.jsx)(d.BZ,{label:"Confirm password",name:"password_confirm",error:null===(n=v.password_confirm)||void 0===n?void 0:n.message,help:"Enter the same password again.",children:(0,s.jsx)(d.II,{type:"password",...b("password_confirm")})}),(0,s.jsx)("div",{className:"flex flex-row justify-center",children:(0,s.jsx)(u.Z,{type:"submit",variant:"primary",children:"Create account"})})]})}var f=r(57126);function g(){let e=(0,i.useRouter)(),t=(0,o.useCallback)(t=>{a.ZP.promise(t.then(t=>(e.push("/login"),t)),{loading:"Creating account...",success:"Account created!",error:"Failed to create account"})},[e]),r=(0,o.useCallback)(()=>{a.ZP.error("This is not your first time here, is it?"),e.push("/login")},[e]);return(0,s.jsx)("div",{className:"flex flex-col items-center justify-center min-h-screen",children:(0,s.jsxs)("div",{className:"flex flex-col max-w-prose gap-4",children:[(0,s.jsxs)("div",{className:"mb-4 flex flex-col items-center gap-4 text-center text-7xl",children:[(0,s.jsx)(n.b_,{width:128,height:128}),(0,s.jsx)("span",{className:"font-sans font-bold text-emerald-500 underline decoration-8",children:"Whombat"})]}),(0,s.jsx)("h1",{className:"text-3xl font-bold text-center",children:"Welcome!"}),(0,s.jsx)("p",{className:"max-w-prose text-center",children:"Let's get started by creating your account. Provide your information and set up a secure password below."}),(0,s.jsx)(b,{onCreate:t,onAuthenticationError:r}),(0,s.jsx)(f.Z,{children:(0,s.jsx)("p",{className:"text-sm max-w-prose text-center",children:"Your data is stored locally on your computer and is not sent to any server."})})]})})}},68447:function(e,t,r){"use strict";r.d(t,{y:function(){return l}});var s=r(57437),o=r(54440),a=r.n(o),i=r(2265);let n={filled:{primary:"border-emerald-500 bg-emerald-300 hover:bg-emerald-500 dark:bg-emerald-600 dark:hover:bg-emerald-700 dark:ring-offset-opacity-50 disabled:bg-emerald-300 dark:disabled:bg-emerald-700",secondary:"border-stone-300 dark:border-stone-600 bg-stone-100 hover:bg-stone-200 dark:bg-stone-700 dark:hover:bg-stone-800 disabled:bg-stone-300 dark:disabled:bg-stone-700 dark:text-stone-400",danger:"border-rose-500 bg-rose-700 hover:bg-rose-800 dark:bg-rose-600 dark:hover:bg-rose-700 disabled:bg-rose-300 dark:disabled:bg-rose-700",success:"border-green-500 bg-green-700 hover:bg-green-800 dark:bg-green-600 dark:hover:bg-green-700 disabled:bg-green-300 dark:disabled:bg-green-700",warning:"border-yellow-500 bg-yellow-700 hover:bg-yellow-800 dark:bg-yellow-600 dark:hover:bg-yellow-700 disabled:bg-yellow-300 dark:disabled:bg-yellow-700",info:"border-blue-500 bg-blue-700 hover:bg-blue-800 dark:bg-blue-600 dark:hover:bg-blue-700 disabled:bg-blue-300 dark:disabled:bg-blue-700",common:"border text-stone-900 dark:text-stone-100 disabled:text-stone-500 dark:disabled:text-stone-300"},outline:{primary:"border-emerald-500 hover:bg-emerald-300 dark:hover:bg-emerald-700",secondary:"border-stone-500 hover:bg-stone-300 dark:hover:bg-stone-700",danger:"border-rose-500 hover:bg-rose-300 dark:hover:bg-rose-700",success:"border-green-500 hover:bg-green-300 dark:hover:bg-green-700",warning:"border-yellow-500 hover:bg-yellow-300 dark:hover:bg-yellow-700",info:"border-blue-500 hover:bg-blue-300 dark:hover:bg-blue-700",common:"border bg-transparent text-stone-900 dark:text-stone-100"},text:{primary:"text-emerald-500 stroke-emerald-500 hover:stroke-emerald-300 dark:hover:stroke-emerald-800",secondary:"text-stone-500 stroke-stone-500 hover:stroke-stone-800 dark:hover:stroke-stone-300 disabled:stroke-stone-500 dark:disabled:stroke-stone-500",danger:"text-rose-500 stroke-rose-500 hover:stroke-rose-300 dark:hover:stroke-rose-800",success:"text-green-500 stroke-green-500 hover:stroke-green-300 dark:hover:stroke-green-800",warning:"text-yellow-500 stroke-yellow-500 hover:stroke-yellow-300 dark:hover:stroke-yellow-800",info:"text-blue-500 stroke-blue-500 hover:stroke-blue-300 dark:hover:stroke-blue-800",common:"bg-transparent hover:underline hover:decoration-solid hover:decoration-2 hover:underline-offset-2 hover:font-extrabold disabled:no-underline disabled:font-medium stroke-2 hover:stroke-4 disabled:stroke-1"}};function l(e){let{variant:t="primary",mode:r="filled",padding:s="p-2.5"}=e;return a()(n[r][t],n[r].common,"focus:ring-4 focus:ring-emerald-500/50 focus:outline-none",s,"group flex flex-row items-center rounded-lg text-center text-sm font-medium")}let d=(0,i.forwardRef)(function(e,t){let{children:r,variant:o="primary",mode:i="filled",padding:n="p-2.5",className:d,...u}=e,c=l({variant:o,mode:i,padding:n});return(0,s.jsx)("button",{className:a()(c,d),...u,ref:t,children:r})});t.Z=d},57126:function(e,t,r){"use strict";r.d(t,{Z:function(){return i}});var s=r(57437),o=r(54440),a=r.n(o);function i(e){let{title:t,className:r,children:o}=e;return(0,s.jsxs)("div",{className:a()(r,"flex items-center p-3 text-sm text-blue-800 border border-blue-300 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400 dark:border-blue-800"),role:"alert",children:[(0,s.jsx)("svg",{className:"flex-shrink-0 inline w-4 h-4 mr-3","aria-hidden":"true",xmlns:"http://www.w3.org/2000/svg",fill:"currentColor",viewBox:"0 0 20 20",children:(0,s.jsx)("path",{d:"M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"})}),(0,s.jsx)("span",{className:"sr-only",children:"Info"}),(0,s.jsxs)("div",{children:[null!=t," ",o]})]})}},24033:function(e,t,r){e.exports=r(15313)},23588:function(e,t,r){"use strict";r.d(t,{D:function(){return c}});var s=r(2265),o=r(77470),a=r(17987),i=r(42996),n=r(40300),l=class extends i.l{constructor(e,t){super(),this.#e=void 0,this.#t=e,this.setOptions(t),this.bindMethods(),this.#r()}#t;#e;#s;#o;bindMethods(){this.mutate=this.mutate.bind(this),this.reset=this.reset.bind(this)}setOptions(e){let t=this.options;this.options=this.#t.defaultMutationOptions(e),(0,n.VS)(t,this.options)||this.#t.getMutationCache().notify({type:"observerOptionsUpdated",mutation:this.#s,observer:this}),this.#s?.setOptions(this.options),t?.mutationKey&&this.options.mutationKey&&(0,n.Ym)(t.mutationKey)!==(0,n.Ym)(this.options.mutationKey)&&this.reset()}onUnsubscribe(){this.hasListeners()||this.#s?.removeObserver(this)}onMutationUpdate(e){this.#r(),this.#a(e)}getCurrentResult(){return this.#e}reset(){this.#s?.removeObserver(this),this.#s=void 0,this.#r(),this.#a()}mutate(e,t){return this.#o=t,this.#s?.removeObserver(this),this.#s=this.#t.getMutationCache().build(this.#t,this.options),this.#s.addObserver(this),this.#s.execute(e)}#r(){let e=this.#s?.state??(0,o.R)();this.#e={...e,isPending:"pending"===e.status,isSuccess:"success"===e.status,isError:"error"===e.status,isIdle:"idle"===e.status,mutate:this.mutate,reset:this.reset}}#a(e){a.V.batch(()=>{this.#o&&this.hasListeners()&&(e?.type==="success"?(this.#o.onSuccess?.(e.data,this.#e.variables,this.#e.context),this.#o.onSettled?.(e.data,null,this.#e.variables,this.#e.context)):e?.type==="error"&&(this.#o.onError?.(e.error,this.#e.variables,this.#e.context),this.#o.onSettled?.(void 0,e.error,this.#e.variables,this.#e.context))),this.listeners.forEach(e=>{e(this.#e)})})}},d=r(38038),u=r(14805);function c(e,t){let r=(0,d.NL)(t),[o]=s.useState(()=>new l(r,e));s.useEffect(()=>{o.setOptions(e)},[o,e]);let i=s.useSyncExternalStore(s.useCallback(e=>o.subscribe(a.V.batchCalls(e)),[o]),()=>o.getCurrentResult(),()=>o.getCurrentResult()),n=s.useCallback((e,t)=>{o.mutate(e,t).catch(p)},[o]);if(i.error&&(0,u.L)(o.options.throwOnError,[i.error]))throw i.error;return{...i,mutate:n,mutateAsync:i.mutate}}function p(){}},14805:function(e,t,r){"use strict";function s(e,t){return"function"==typeof e?e(...t):!!e}r.d(t,{L:function(){return s}})},5925:function(e,t,r){"use strict";let s,o;r.d(t,{Ih:function(){return et},x7:function(){return ec},ZP:function(){return ep},GK:function(){return E},Am:function(){return z}});var a,i=r(2265);let n={data:""},l=e=>"object"==typeof window?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||n,d=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,u=/\/\*[^]*?\*\/|  +/g,c=/\n+/g,p=(e,t)=>{let r="",s="",o="";for(let a in e){let i=e[a];"@"==a[0]?"i"==a[1]?r=a+" "+i+";":s+="f"==a[1]?p(i,a):a+"{"+p(i,"k"==a[1]?"":t)+"}":"object"==typeof i?s+=p(i,t?t.replace(/([^,])+/g,e=>a.replace(/(^:.*)|([^,])+/g,t=>/&/.test(t)?t.replace(/&/g,e):e?e+" "+t:t)):a):null!=i&&(a=/^--/.test(a)?a:a.replace(/[A-Z]/g,"-$&").toLowerCase(),o+=p.p?p.p(a,i):a+":"+i+";")}return r+(t&&o?t+"{"+o+"}":o)+s},h={},m=e=>{if("object"==typeof e){let t="";for(let r in e)t+=r+m(e[r]);return t}return e},b=(e,t,r,s,o)=>{var a;let i=m(e),n=h[i]||(h[i]=(e=>{let t=0,r=11;for(;t<e.length;)r=101*r+e.charCodeAt(t++)>>>0;return"go"+r})(i));if(!h[n]){let t=i!==e?e:(e=>{let t,r,s=[{}];for(;t=d.exec(e.replace(u,""));)t[4]?s.shift():t[3]?(r=t[3].replace(c," ").trim(),s.unshift(s[0][r]=s[0][r]||{})):s[0][t[1]]=t[2].replace(c," ").trim();return s[0]})(e);h[n]=p(o?{["@keyframes "+n]:t}:t,r?"":"."+n)}let l=r&&h.g?h.g:null;return r&&(h.g=h[n]),a=h[n],l?t.data=t.data.replace(l,a):-1===t.data.indexOf(a)&&(t.data=s?a+t.data:t.data+a),n},f=(e,t,r)=>e.reduce((e,s,o)=>{let a=t[o];if(a&&a.call){let e=a(r),t=e&&e.props&&e.props.className||/^go/.test(e)&&e;a=t?"."+t:e&&"object"==typeof e?e.props?"":p(e,""):!1===e?"":e}return e+s+(null==a?"":a)},"");function g(e){let t=this||{},r=e.call?e(t.p):e;return b(r.unshift?r.raw?f(r,[].slice.call(arguments,1),t.p):r.reduce((e,r)=>Object.assign(e,r&&r.call?r(t.p):r),{}):r,l(t.target),t.g,t.o,t.k)}g.bind({g:1});let v,y,x,k=g.bind({k:1});function w(e,t){let r=this||{};return function(){let s=arguments;function o(a,i){let n=Object.assign({},a),l=n.className||o.className;r.p=Object.assign({theme:y&&y()},n),r.o=/ *go\d+/.test(l),n.className=g.apply(r,s)+(l?" "+l:""),t&&(n.ref=i);let d=e;return e[0]&&(d=n.as||e,delete n.as),x&&d[0]&&x(n),v(d,n)}return t?t(o):o}}var j=e=>"function"==typeof e,E=(e,t)=>j(e)?e(t):e,O=(s=0,()=>(++s).toString()),C=()=>{if(void 0===o&&"u">typeof window){let e=matchMedia("(prefers-reduced-motion: reduce)");o=!e||e.matches}return o},N=new Map,M=e=>{if(N.has(e))return;let t=setTimeout(()=>{N.delete(e),Z({type:4,toastId:e})},1e3);N.set(e,t)},I=e=>{let t=N.get(e);t&&clearTimeout(t)},R=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,20)};case 1:return t.toast.id&&I(t.toast.id),{...e,toasts:e.toasts.map(e=>e.id===t.toast.id?{...e,...t.toast}:e)};case 2:let{toast:r}=t;return e.toasts.find(e=>e.id===r.id)?R(e,{type:1,toast:r}):R(e,{type:0,toast:r});case 3:let{toastId:s}=t;return s?M(s):e.toasts.forEach(e=>{M(e.id)}),{...e,toasts:e.toasts.map(e=>e.id===s||void 0===s?{...e,visible:!1}:e)};case 4:return void 0===t.toastId?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(e=>e.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let o=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(e=>({...e,pauseDuration:e.pauseDuration+o}))}}},$=[],P={toasts:[],pausedAt:void 0},Z=e=>{P=R(P,e),$.forEach(e=>{e(P)})},A={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},S=(e={})=>{let[t,r]=(0,i.useState)(P);(0,i.useEffect)(()=>($.push(r),()=>{let e=$.indexOf(r);e>-1&&$.splice(e,1)}),[t]);let s=t.toasts.map(t=>{var r,s;return{...e,...e[t.type],...t,duration:t.duration||(null==(r=e[t.type])?void 0:r.duration)||(null==e?void 0:e.duration)||A[t.type],style:{...e.style,...null==(s=e[t.type])?void 0:s.style,...t.style}}});return{...t,toasts:s}},_=(e,t="blank",r)=>({createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...r,id:(null==r?void 0:r.id)||O()}),D=e=>(t,r)=>{let s=_(t,e,r);return Z({type:2,toast:s}),s.id},z=(e,t)=>D("blank")(e,t);z.error=D("error"),z.success=D("success"),z.loading=D("loading"),z.custom=D("custom"),z.dismiss=e=>{Z({type:3,toastId:e})},z.remove=e=>Z({type:4,toastId:e}),z.promise=(e,t,r)=>{let s=z.loading(t.loading,{...r,...null==r?void 0:r.loading});return e.then(e=>(z.success(E(t.success,e),{id:s,...r,...null==r?void 0:r.success}),e)).catch(e=>{z.error(E(t.error,e),{id:s,...r,...null==r?void 0:r.error})}),e};var L=(e,t)=>{Z({type:1,toast:{id:e,height:t}})},T=()=>{Z({type:5,time:Date.now()})},F=e=>{let{toasts:t,pausedAt:r}=S(e);(0,i.useEffect)(()=>{if(r)return;let e=Date.now(),s=t.map(t=>{if(t.duration===1/0)return;let r=(t.duration||0)+t.pauseDuration-(e-t.createdAt);if(r<0){t.visible&&z.dismiss(t.id);return}return setTimeout(()=>z.dismiss(t.id),r)});return()=>{s.forEach(e=>e&&clearTimeout(e))}},[t,r]);let s=(0,i.useCallback)(()=>{r&&Z({type:6,time:Date.now()})},[r]),o=(0,i.useCallback)((e,r)=>{let{reverseOrder:s=!1,gutter:o=8,defaultPosition:a}=r||{},i=t.filter(t=>(t.position||a)===(e.position||a)&&t.height),n=i.findIndex(t=>t.id===e.id),l=i.filter((e,t)=>t<n&&e.visible).length;return i.filter(e=>e.visible).slice(...s?[l+1]:[0,l]).reduce((e,t)=>e+(t.height||0)+o,0)},[t]);return{toasts:t,handlers:{updateHeight:L,startPause:T,endPause:s,calculateOffset:o}}},B=k`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,H=k`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,U=k`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,K=w("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${B} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${H} 0.15s ease-out forwards;
    animation-delay: 150ms;
    position: absolute;
    border-radius: 3px;
    opacity: 0;
    background: ${e=>e.secondary||"#fff"};
    bottom: 9px;
    left: 4px;
    height: 2px;
    width: 12px;
  }

  &:before {
    animation: ${U} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,Y=k`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,V=w("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${Y} 1s linear infinite;
`,W=k`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,q=k`
0% {
	height: 0;
	width: 0;
	opacity: 0;
}
40% {
  height: 0;
	width: 6px;
	opacity: 1;
}
100% {
  opacity: 1;
  height: 10px;
}`,G=w("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${W} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${q} 0.2s ease-out forwards;
    opacity: 0;
    animation-delay: 200ms;
    position: absolute;
    border-right: 2px solid;
    border-bottom: 2px solid;
    border-color: ${e=>e.secondary||"#fff"};
    bottom: 6px;
    left: 6px;
    height: 10px;
    width: 6px;
  }
`,J=w("div")`
  position: absolute;
`,Q=w("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,X=k`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,ee=w("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${X} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,et=({toast:e})=>{let{icon:t,type:r,iconTheme:s}=e;return void 0!==t?"string"==typeof t?i.createElement(ee,null,t):t:"blank"===r?null:i.createElement(Q,null,i.createElement(V,{...s}),"loading"!==r&&i.createElement(J,null,"error"===r?i.createElement(K,{...s}):i.createElement(G,{...s})))},er=e=>`
0% {transform: translate3d(0,${-200*e}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,es=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*e}%,-1px) scale(.6); opacity:0;}
`,eo=w("div")`
  display: flex;
  align-items: center;
  background: #fff;
  color: #363636;
  line-height: 1.3;
  will-change: transform;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1), 0 3px 3px rgba(0, 0, 0, 0.05);
  max-width: 350px;
  pointer-events: auto;
  padding: 8px 10px;
  border-radius: 8px;
`,ea=w("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,ei=(e,t)=>{let r=e.includes("top")?1:-1,[s,o]=C()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[er(r),es(r)];return{animation:t?`${k(s)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${k(o)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},en=i.memo(({toast:e,position:t,style:r,children:s})=>{let o=e.height?ei(e.position||t||"top-center",e.visible):{opacity:0},a=i.createElement(et,{toast:e}),n=i.createElement(ea,{...e.ariaProps},E(e.message,e));return i.createElement(eo,{className:e.className,style:{...o,...r,...e.style}},"function"==typeof s?s({icon:a,message:n}):i.createElement(i.Fragment,null,a,n))});a=i.createElement,p.p=void 0,v=a,y=void 0,x=void 0;var el=({id:e,className:t,style:r,onHeightUpdate:s,children:o})=>{let a=i.useCallback(t=>{if(t){let r=()=>{s(e,t.getBoundingClientRect().height)};r(),new MutationObserver(r).observe(t,{subtree:!0,childList:!0,characterData:!0})}},[e,s]);return i.createElement("div",{ref:a,className:t,style:r},o)},ed=(e,t)=>{let r=e.includes("top"),s=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:C()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(r?1:-1)}px)`,...r?{top:0}:{bottom:0},...s}},eu=g`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,ec=({reverseOrder:e,position:t="top-center",toastOptions:r,gutter:s,children:o,containerStyle:a,containerClassName:n})=>{let{toasts:l,handlers:d}=F(r);return i.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...a},className:n,onMouseEnter:d.startPause,onMouseLeave:d.endPause},l.map(r=>{let a=r.position||t,n=ed(a,d.calculateOffset(r,{reverseOrder:e,gutter:s,defaultPosition:t}));return i.createElement(el,{id:r.id,key:r.id,onHeightUpdate:d.updateHeight,className:r.visible?eu:"",style:n},"custom"===r.type?E(r.message,r):o?o(r):i.createElement(en,{toast:r,position:a}))}))},ep=z}},function(e){e.O(0,[1749,9966,3475,8966,828,721,1698,262,2971,4938,1744],function(){return e(e.s=59359)}),_N_E=e.O()}]);