(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1165],{37667:function(t,e,r){Promise.resolve().then(r.bind(r,94441))},94441:function(t,e,r){"use strict";r.r(e),r.d(e,{default:function(){return p}});var s=r(57437),i=r(23588),n=r(24033),o=r(61865),a=r(5925),l=r(81698),c=r(37275),u=r(45987),d=r(90262);function p(){var t;let e=(0,n.useRouter)(),{register:r,handleSubmit:p,setError:m,formState:{errors:f}}=(0,o.cI)({mode:"onChange"}),{mutateAsync:h}=(0,i.D)({mutationFn:l.Z.annotationProjects.import,onError:t=>{var e;(null===(e=t.response)||void 0===e?void 0:e.status)===422&&t.response.data.detail.forEach(t=>{m(t.loc[1],{message:t.msg})})},onSuccess:t=>{e.push("/annotation_projects/detail/?annotation_project_uuid=".concat(t.uuid))}}),b=async t=>{let e=new FormData,r=t.annotation_project[0];return e.append("annotation_project",r),await a.ZP.promise(h(e),{loading:"Importing annotation project. Please wait, it can take some time...",success:"Annotation project imported successfully!",error:"Failed to import annotation project."})};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(c.Z,{text:"Import an Annotation Project"}),(0,s.jsx)("div",{className:"flex w-full flex-col justify-center items-center p-16",children:(0,s.jsxs)("form",{className:"flex flex-col gap-4",onSubmit:p(b),children:[(0,s.jsx)(d.BZ,{name:"annotation_project",label:"Select a project file to import",help:"The file must be in AOEF format",error:null===(t=f.file)||void 0===t?void 0:t.message,children:(0,s.jsx)(d.II,{type:"file",...r("annotation_project"),required:!0})}),(0,s.jsxs)(d.k4,{children:[(0,s.jsx)(u.rG,{className:"inline-block h-6 w-6 align-middle mr-2"}),"Import"]})]})})]})}},45518:function(t,e,r){"use strict";r.d(e,{Z:function(){return i}});var s=r(57437);function i(t){let{children:e}=t;return(0,s.jsx)("header",{className:"bg-stone-50 shadow dark:bg-stone-800",children:(0,s.jsx)("div",{className:"max-w-7xl px-2 py-3 sm:px-3 lg:px-6",children:e})})}},2964:function(t,e,r){"use strict";r.d(e,{H1:function(){return o},H2:function(){return a},H3:function(){return l},H4:function(){return c}});var s=r(57437),i=r(54440),n=r.n(i);function o(t){let{children:e,className:r,...i}=t;return(0,s.jsx)("h1",{className:n()("text-2xl font-bold text-stone-800 dark:text-stone-300",r),...i,children:e})}function a(t){let{children:e,className:r,...i}=t;return(0,s.jsx)("h2",{className:n()("text-xl font-bold text-stone-800 dark:text-stone-300",r),...i,children:e})}function l(t){let{children:e,className:r,...i}=t;return(0,s.jsx)("h3",{className:n()("text-lg font-semibold leading-7 items-center text-stone-800 dark:text-stone-300",r),...i,children:e})}function c(t){let{children:e,className:r,...i}=t;return(0,s.jsx)("h4",{className:n()(r,"text-md font-semibold leading-6 text-stone-800 dark:text-stone-300"),...i,children:e})}},37275:function(t,e,r){"use strict";r.d(e,{Z:function(){return o}});var s=r(57437),i=r(45518),n=r(2964);function o(t){let{text:e}=t;return(0,s.jsx)(i.Z,{children:(0,s.jsx)(n.H1,{children:e})})}},24033:function(t,e,r){t.exports=r(15313)},23588:function(t,e,r){"use strict";r.d(e,{D:function(){return d}});var s=r(2265),i=r(77470),n=r(17987),o=r(42996),a=r(40300),l=class extends o.l{constructor(t,e){super(),this.#t=void 0,this.#e=t,this.setOptions(e),this.bindMethods(),this.#r()}#e;#t;#s;#i;bindMethods(){this.mutate=this.mutate.bind(this),this.reset=this.reset.bind(this)}setOptions(t){let e=this.options;this.options=this.#e.defaultMutationOptions(t),(0,a.VS)(e,this.options)||this.#e.getMutationCache().notify({type:"observerOptionsUpdated",mutation:this.#s,observer:this}),this.#s?.setOptions(this.options),e?.mutationKey&&this.options.mutationKey&&(0,a.Ym)(e.mutationKey)!==(0,a.Ym)(this.options.mutationKey)&&this.reset()}onUnsubscribe(){this.hasListeners()||this.#s?.removeObserver(this)}onMutationUpdate(t){this.#r(),this.#n(t)}getCurrentResult(){return this.#t}reset(){this.#s?.removeObserver(this),this.#s=void 0,this.#r(),this.#n()}mutate(t,e){return this.#i=e,this.#s?.removeObserver(this),this.#s=this.#e.getMutationCache().build(this.#e,this.options),this.#s.addObserver(this),this.#s.execute(t)}#r(){let t=this.#s?.state??(0,i.R)();this.#t={...t,isPending:"pending"===t.status,isSuccess:"success"===t.status,isError:"error"===t.status,isIdle:"idle"===t.status,mutate:this.mutate,reset:this.reset}}#n(t){n.V.batch(()=>{this.#i&&this.hasListeners()&&(t?.type==="success"?(this.#i.onSuccess?.(t.data,this.#t.variables,this.#t.context),this.#i.onSettled?.(t.data,null,this.#t.variables,this.#t.context)):t?.type==="error"&&(this.#i.onError?.(t.error,this.#t.variables,this.#t.context),this.#i.onSettled?.(void 0,t.error,this.#t.variables,this.#t.context))),this.listeners.forEach(t=>{t(this.#t)})})}},c=r(38038),u=r(14805);function d(t,e){let r=(0,c.NL)(e),[i]=s.useState(()=>new l(r,t));s.useEffect(()=>{i.setOptions(t)},[i,t]);let o=s.useSyncExternalStore(s.useCallback(t=>i.subscribe(n.V.batchCalls(t)),[i]),()=>i.getCurrentResult(),()=>i.getCurrentResult()),a=s.useCallback((t,e)=>{i.mutate(t,e).catch(p)},[i]);if(o.error&&(0,u.L)(i.options.throwOnError,[o.error]))throw o.error;return{...o,mutate:a,mutateAsync:o.mutate}}function p(){}},14805:function(t,e,r){"use strict";function s(t,e){return"function"==typeof t?t(...e):!!t}r.d(e,{L:function(){return s}})},5925:function(t,e,r){"use strict";let s,i;r.d(e,{Ih:function(){return te},x7:function(){return td},ZP:function(){return tp},GK:function(){return O},Am:function(){return F}});var n,o=r(2265);let a={data:""},l=t=>"object"==typeof window?((t?t.querySelector("#_goober"):window._goober)||Object.assign((t||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:t||a,c=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,u=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,p=(t,e)=>{let r="",s="",i="";for(let n in t){let o=t[n];"@"==n[0]?"i"==n[1]?r=n+" "+o+";":s+="f"==n[1]?p(o,n):n+"{"+p(o,"k"==n[1]?"":e)+"}":"object"==typeof o?s+=p(o,e?e.replace(/([^,])+/g,t=>n.replace(/(^:.*)|([^,])+/g,e=>/&/.test(e)?e.replace(/&/g,t):t?t+" "+e:e)):n):null!=o&&(n=/^--/.test(n)?n:n.replace(/[A-Z]/g,"-$&").toLowerCase(),i+=p.p?p.p(n,o):n+":"+o+";")}return r+(e&&i?e+"{"+i+"}":i)+s},m={},f=t=>{if("object"==typeof t){let e="";for(let r in t)e+=r+f(t[r]);return e}return t},h=(t,e,r,s,i)=>{var n;let o=f(t),a=m[o]||(m[o]=(t=>{let e=0,r=11;for(;e<t.length;)r=101*r+t.charCodeAt(e++)>>>0;return"go"+r})(o));if(!m[a]){let e=o!==t?t:(t=>{let e,r,s=[{}];for(;e=c.exec(t.replace(u,""));)e[4]?s.shift():e[3]?(r=e[3].replace(d," ").trim(),s.unshift(s[0][r]=s[0][r]||{})):s[0][e[1]]=e[2].replace(d," ").trim();return s[0]})(t);m[a]=p(i?{["@keyframes "+a]:e}:e,r?"":"."+a)}let l=r&&m.g?m.g:null;return r&&(m.g=m[a]),n=m[a],l?e.data=e.data.replace(l,n):-1===e.data.indexOf(n)&&(e.data=s?n+e.data:e.data+n),a},b=(t,e,r)=>t.reduce((t,s,i)=>{let n=e[i];if(n&&n.call){let t=n(r),e=t&&t.props&&t.props.className||/^go/.test(t)&&t;n=e?"."+e:t&&"object"==typeof t?t.props?"":p(t,""):!1===t?"":t}return t+s+(null==n?"":n)},"");function g(t){let e=this||{},r=t.call?t(e.p):t;return h(r.unshift?r.raw?b(r,[].slice.call(arguments,1),e.p):r.reduce((t,r)=>Object.assign(t,r&&r.call?r(e.p):r),{}):r,l(e.target),e.g,e.o,e.k)}g.bind({g:1});let y,x,v,w=g.bind({k:1});function j(t,e){let r=this||{};return function(){let s=arguments;function i(n,o){let a=Object.assign({},n),l=a.className||i.className;r.p=Object.assign({theme:x&&x()},a),r.o=/ *go\d+/.test(l),a.className=g.apply(r,s)+(l?" "+l:""),e&&(a.ref=o);let c=t;return t[0]&&(c=a.as||t,delete a.as),v&&c[0]&&v(a),y(c,a)}return e?e(i):i}}var E=t=>"function"==typeof t,O=(t,e)=>E(t)?t(e):t,k=(s=0,()=>(++s).toString()),N=()=>{if(void 0===i&&"u">typeof window){let t=matchMedia("(prefers-reduced-motion: reduce)");i=!t||t.matches}return i},C=new Map,M=t=>{if(C.has(t))return;let e=setTimeout(()=>{C.delete(t),_({type:4,toastId:t})},1e3);C.set(t,e)},R=t=>{let e=C.get(t);e&&clearTimeout(e)},$=(t,e)=>{switch(e.type){case 0:return{...t,toasts:[e.toast,...t.toasts].slice(0,20)};case 1:return e.toast.id&&R(e.toast.id),{...t,toasts:t.toasts.map(t=>t.id===e.toast.id?{...t,...e.toast}:t)};case 2:let{toast:r}=e;return t.toasts.find(t=>t.id===r.id)?$(t,{type:1,toast:r}):$(t,{type:0,toast:r});case 3:let{toastId:s}=e;return s?M(s):t.toasts.forEach(t=>{M(t.id)}),{...t,toasts:t.toasts.map(t=>t.id===s||void 0===s?{...t,visible:!1}:t)};case 4:return void 0===e.toastId?{...t,toasts:[]}:{...t,toasts:t.toasts.filter(t=>t.id!==e.toastId)};case 5:return{...t,pausedAt:e.time};case 6:let i=e.time-(t.pausedAt||0);return{...t,pausedAt:void 0,toasts:t.toasts.map(t=>({...t,pauseDuration:t.pauseDuration+i}))}}},I=[],S={toasts:[],pausedAt:void 0},_=t=>{S=$(S,t),I.forEach(t=>{t(S)})},A={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},P=(t={})=>{let[e,r]=(0,o.useState)(S);(0,o.useEffect)(()=>(I.push(r),()=>{let t=I.indexOf(r);t>-1&&I.splice(t,1)}),[e]);let s=e.toasts.map(e=>{var r,s;return{...t,...t[e.type],...e,duration:e.duration||(null==(r=t[e.type])?void 0:r.duration)||(null==t?void 0:t.duration)||A[e.type],style:{...t.style,...null==(s=t[e.type])?void 0:s.style,...e.style}}});return{...e,toasts:s}},D=(t,e="blank",r)=>({createdAt:Date.now(),visible:!0,type:e,ariaProps:{role:"status","aria-live":"polite"},message:t,pauseDuration:0,...r,id:(null==r?void 0:r.id)||k()}),z=t=>(e,r)=>{let s=D(e,t,r);return _({type:2,toast:s}),s.id},F=(t,e)=>z("blank")(t,e);F.error=z("error"),F.success=z("success"),F.loading=z("loading"),F.custom=z("custom"),F.dismiss=t=>{_({type:3,toastId:t})},F.remove=t=>_({type:4,toastId:t}),F.promise=(t,e,r)=>{let s=F.loading(e.loading,{...r,...null==r?void 0:r.loading});return t.then(t=>(F.success(O(e.success,t),{id:s,...r,...null==r?void 0:r.success}),t)).catch(t=>{F.error(O(e.error,t),{id:s,...r,...null==r?void 0:r.error})}),t};var H=(t,e)=>{_({type:1,toast:{id:t,height:e}})},L=()=>{_({type:5,time:Date.now()})},Z=t=>{let{toasts:e,pausedAt:r}=P(t);(0,o.useEffect)(()=>{if(r)return;let t=Date.now(),s=e.map(e=>{if(e.duration===1/0)return;let r=(e.duration||0)+e.pauseDuration-(t-e.createdAt);if(r<0){e.visible&&F.dismiss(e.id);return}return setTimeout(()=>F.dismiss(e.id),r)});return()=>{s.forEach(t=>t&&clearTimeout(t))}},[e,r]);let s=(0,o.useCallback)(()=>{r&&_({type:6,time:Date.now()})},[r]),i=(0,o.useCallback)((t,r)=>{let{reverseOrder:s=!1,gutter:i=8,defaultPosition:n}=r||{},o=e.filter(e=>(e.position||n)===(t.position||n)&&e.height),a=o.findIndex(e=>e.id===t.id),l=o.filter((t,e)=>e<a&&t.visible).length;return o.filter(t=>t.visible).slice(...s?[l+1]:[0,l]).reduce((t,e)=>t+(e.height||0)+i,0)},[e]);return{toasts:e,handlers:{updateHeight:H,startPause:L,endPause:s,calculateOffset:i}}},T=w`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,K=w`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,U=w`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,V=j("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${t=>t.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${T} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${K} 0.15s ease-out forwards;
    animation-delay: 150ms;
    position: absolute;
    border-radius: 3px;
    opacity: 0;
    background: ${t=>t.secondary||"#fff"};
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
`,Y=w`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,q=j("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${t=>t.secondary||"#e0e0e0"};
  border-right-color: ${t=>t.primary||"#616161"};
  animation: ${Y} 1s linear infinite;
`,B=w`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,G=w`
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
}`,J=j("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${t=>t.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${B} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${G} 0.2s ease-out forwards;
    opacity: 0;
    animation-delay: 200ms;
    position: absolute;
    border-right: 2px solid;
    border-bottom: 2px solid;
    border-color: ${t=>t.secondary||"#fff"};
    bottom: 6px;
    left: 6px;
    height: 10px;
    width: 6px;
  }
`,Q=j("div")`
  position: absolute;
`,W=j("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,X=w`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,tt=j("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${X} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,te=({toast:t})=>{let{icon:e,type:r,iconTheme:s}=t;return void 0!==e?"string"==typeof e?o.createElement(tt,null,e):e:"blank"===r?null:o.createElement(W,null,o.createElement(q,{...s}),"loading"!==r&&o.createElement(Q,null,"error"===r?o.createElement(V,{...s}):o.createElement(J,{...s})))},tr=t=>`
0% {transform: translate3d(0,${-200*t}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,ts=t=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*t}%,-1px) scale(.6); opacity:0;}
`,ti=j("div")`
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
`,tn=j("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,to=(t,e)=>{let r=t.includes("top")?1:-1,[s,i]=N()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[tr(r),ts(r)];return{animation:e?`${w(s)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${w(i)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},ta=o.memo(({toast:t,position:e,style:r,children:s})=>{let i=t.height?to(t.position||e||"top-center",t.visible):{opacity:0},n=o.createElement(te,{toast:t}),a=o.createElement(tn,{...t.ariaProps},O(t.message,t));return o.createElement(ti,{className:t.className,style:{...i,...r,...t.style}},"function"==typeof s?s({icon:n,message:a}):o.createElement(o.Fragment,null,n,a))});n=o.createElement,p.p=void 0,y=n,x=void 0,v=void 0;var tl=({id:t,className:e,style:r,onHeightUpdate:s,children:i})=>{let n=o.useCallback(e=>{if(e){let r=()=>{s(t,e.getBoundingClientRect().height)};r(),new MutationObserver(r).observe(e,{subtree:!0,childList:!0,characterData:!0})}},[t,s]);return o.createElement("div",{ref:n,className:e,style:r},i)},tc=(t,e)=>{let r=t.includes("top"),s=t.includes("center")?{justifyContent:"center"}:t.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:N()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${e*(r?1:-1)}px)`,...r?{top:0}:{bottom:0},...s}},tu=g`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,td=({reverseOrder:t,position:e="top-center",toastOptions:r,gutter:s,children:i,containerStyle:n,containerClassName:a})=>{let{toasts:l,handlers:c}=Z(r);return o.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...n},className:a,onMouseEnter:c.startPause,onMouseLeave:c.endPause},l.map(r=>{let n=r.position||e,a=tc(n,c.calculateOffset(r,{reverseOrder:t,gutter:s,defaultPosition:e}));return o.createElement(tl,{id:r.id,key:r.id,onHeightUpdate:c.updateHeight,className:r.visible?tu:"",style:a},"custom"===r.type?O(r.message,r):i?i(r):o.createElement(ta,{toast:r,position:n}))}))},tp=F}},function(t){t.O(0,[1749,9966,3475,8966,828,721,1698,262,2971,4938,1744],function(){return t(t.s=37667)}),_N_E=t.O()}]);