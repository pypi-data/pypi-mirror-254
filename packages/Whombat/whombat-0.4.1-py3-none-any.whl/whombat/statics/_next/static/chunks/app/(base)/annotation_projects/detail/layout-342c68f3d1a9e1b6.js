(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1788],{54598:function(t,e,n){Promise.resolve().then(n.bind(n,44711))},83007:function(t,e,n){"use strict";let r=(0,n(2265).createContext)({name:"",description:"",tags:[],created_on:new Date,uuid:""});e.Z=r},44711:function(t,e,n){"use strict";n.r(e),n.d(e,{default:function(){return h}});var r=n(57437),o=n(24033),i=n(5925),s=n(7933),a=n(45518),u=n(2964),c=n(45987),l=n(42944);function d(t){let{annotationProject:e}=t,n=(0,o.useRouter)(),i=(0,o.useSearchParams)(),s=(0,o.useSelectedLayoutSegment)();return(0,r.jsx)(a.Z,{children:(0,r.jsxs)("div",{className:"flex overflow-x-auto flex-row space-x-4 w-full",children:[(0,r.jsx)(u.H1,{className:"overflow-auto max-w-xl whitespace-nowrap",children:e.name}),(0,r.jsx)(l.Z,{tabs:[{id:"overview",title:"Overview",isActive:null===s,icon:(0,r.jsx)(c.lQ,{className:"w-5 h-5 align-middle"}),onClick:()=>{n.push("/annotation_projects/detail/?".concat(i.toString()))}},{id:"annotate",title:"Annotate",isActive:"annotation"===s,icon:(0,r.jsx)(c.dY,{className:"w-5 h-5 align-middle"}),onClick:()=>{n.push("/annotation_projects/detail/annotation/?".concat(i.toString()))}},{id:"tasks",title:"Tasks",isActive:"tasks"===s,icon:(0,r.jsx)(c.Fl,{className:"w-5 h-5 align-middle"}),onClick:()=>{n.push("/annotation_projects/detail/tasks/?".concat(i.toString()))}},{id:"tags",title:"Tags",isActive:"tags"===s,icon:(0,r.jsx)(c.Dg,{className:"w-5 h-5 align-middle"}),onClick:()=>{n.push("/annotation_projects/detail/tags/?".concat(i.toString()))}}]})]})})}var f=n(17968),p=n(83007);function h(t){let{children:e}=t,n=(0,o.useSearchParams)(),a=(0,o.useRouter)(),u=n.get("annotation_project_uuid");null==u&&(i.Am.error("Annotation project uuid not specified."),a.push("/annotation_projects/"));let c=(0,f.Z)({uuid:u});if(c.isLoading)return(0,r.jsx)(s.Z,{});if(c.isError||null==c.data){i.Am.error("Annotation project not found."),a.push("/annotation_projects/");return}return(0,r.jsxs)(p.Z.Provider,{value:c.data,children:[(0,r.jsx)(d,{annotationProject:c.data}),(0,r.jsx)("div",{className:"p-4",children:e})]})}},7933:function(t,e,n){"use strict";n.d(e,{Z:function(){return i}});var r=n(57437),o=n(25137);function i(){return(0,r.jsx)("div",{className:"w-full h-full flex flex-row justify-center items-center",children:(0,r.jsx)(o.Z,{})})}},45518:function(t,e,n){"use strict";n.d(e,{Z:function(){return o}});var r=n(57437);function o(t){let{children:e}=t;return(0,r.jsx)("header",{className:"bg-stone-50 shadow dark:bg-stone-800",children:(0,r.jsx)("div",{className:"max-w-7xl px-2 py-3 sm:px-3 lg:px-6",children:e})})}},2964:function(t,e,n){"use strict";n.d(e,{H1:function(){return s},H2:function(){return a},H3:function(){return u},H4:function(){return c}});var r=n(57437),o=n(54440),i=n.n(o);function s(t){let{children:e,className:n,...o}=t;return(0,r.jsx)("h1",{className:i()("text-2xl font-bold text-stone-800 dark:text-stone-300",n),...o,children:e})}function a(t){let{children:e,className:n,...o}=t;return(0,r.jsx)("h2",{className:i()("text-xl font-bold text-stone-800 dark:text-stone-300",n),...o,children:e})}function u(t){let{children:e,className:n,...o}=t;return(0,r.jsx)("h3",{className:i()("text-lg font-semibold leading-7 items-center text-stone-800 dark:text-stone-300",n),...o,children:e})}function c(t){let{children:e,className:n,...o}=t;return(0,r.jsx)("h4",{className:i()(n,"text-md font-semibold leading-6 text-stone-800 dark:text-stone-300"),...o,children:e})}},25137:function(t,e,n){"use strict";n.d(e,{Z:function(){return s}});var r=n(57437),o=n(54440),i=n.n(o);function s(t){let{variant:e="primary",className:n="w-8 h-8"}=t;return(0,r.jsxs)("div",{role:"status",children:[(0,r.jsxs)("svg",{"aria-hidden":"true",className:i()(n,"mr-2 inline animate-spin text-stone-200 dark:text-stone-600",function(t){switch(t){case"primary":case"success":return"fill-emerald-500";case"secondary":return"fill-stone-900 dark:fill-stone-100";case"danger":return"fill-rose-500";case"warning":return"fill-yellow-500";case"info":return"fill-blue-500"}}(e)),viewBox:"0 0 100 101",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,r.jsx)("path",{d:"M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z",fill:"currentColor"}),(0,r.jsx)("path",{d:"M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z",fill:"currentFill"})]}),(0,r.jsx)("span",{className:"sr-only",children:"Loading..."})]})}},42944:function(t,e,n){"use strict";n.d(e,{Z:function(){return p}});var r=n(57437),o=n(54440),i=n.n(o),s=n(61396),a=n.n(s);let u="whitespace-nowrap rounded-lg bg-stone-50 p-2 text-center text-sm font-medium dark:bg-stone-800 focus:outline-none focus:ring-4 focus:ring-emerald-500/50",c="text-emerald-500",l="text-stone-700 hover:bg-stone-200 hover:text-stone-900 dark:text-stone-400 dark:hover:bg-stone-700 dark:hover:text-stone-300";function d(t){let{children:e,active:n=!1,className:o,...s}=t;return(0,r.jsx)("button",{...s,className:i()(u,n?c:l,o),children:e})}function f(t){let{children:e,active:n=!1,className:o,...s}=t;return(0,r.jsx)(a(),{...s,className:i()(u,n?c:l,o,"p-2 inline-block"),children:e})}function p(t){let{tabs:e}=t;return(0,r.jsx)("ul",{className:"flex space-x-4",children:e.map(t=>(0,r.jsx)("li",{children:null!=t.href?(0,r.jsxs)(f,{href:t.href,active:t.isActive,children:[t.icon?(0,r.jsx)("span",{className:"mr-1 inline-block align-middle",children:t.icon}):null,t.title]}):(0,r.jsxs)(d,{onClick:t.onClick,active:t.isActive,children:[t.icon?(0,r.jsx)("span",{className:"mr-1 inline-block align-middle",children:t.icon}):null,t.title]})},t.id))})}},45987:function(t,e,n){"use strict";n.d(e,{A5:function(){return s.Z},Al:function(){return tn.Z},An:function(){return G.Z},Dd:function(){return A.Z},Dg:function(){return to.Z},Dj:function(){return a.Z},E6:function(){return J.Z},Fl:function(){return N.Z},Fr:function(){return X.Z},GV:function(){return S.Z},He:function(){return R.Z},Hl:function(){return u.Z},IH:function(){return x.Z},Iz:function(){return ty},N$:function(){return m.Z},NW:function(){return tp.Z},Ne:function(){return l.Z},O4:function(){return B.Z},OA:function(){return tf.Z},OZ:function(){return C.Z},Op:function(){return Z.Z},P1:function(){return L.Z},QE:function(){return h.Z},Qq:function(){return k.Z},Qu:function(){return v.Z},RJ:function(){return tl.Z},SA:function(){return tt.Z},Tw:function(){return tu.Z},VE:function(){return tj},Vn:function(){return q.Z},Vr:function(){return td.Z},W1:function(){return T.Z},X$:function(){return E.Z},ZA:function(){return tc.Z},Zi:function(){return b.Z},Zl:function(){return z.Z},_8:function(){return i.Z},_t:function(){return Q.Z},aN:function(){return V.Z},b_:function(){return tb},by:function(){return tg.Z},cV:function(){return w.Z},cX:function(){return F.Z},dY:function(){return W.Z},dt:function(){return Y.Z},ew:function(){return O.Z},fp:function(){return K.Z},i5:function(){return p.Z},jE:function(){return tw},jJ:function(){return c.Z},k1:function(){return D.Z},lO:function(){return ti.Z},lQ:function(){return o.Z},nQ:function(){return j.Z},nU:function(){return $.Z},o1:function(){return U.Z},oE:function(){return th.Z},pJ:function(){return ts.Z},rG:function(){return d.Z},rj:function(){return g.Z},rm:function(){return tm.Z},sH:function(){return te.Z},se:function(){return _.Z},tB:function(){return ta.Z},tv:function(){return I.Z},uH:function(){return y.Z},uN:function(){return H.Z},wZ:function(){return M.Z},wv:function(){return P.Z},xC:function(){return f.Z},yb:function(){return tZ},zB:function(){return tr.Z}});var r=n(57437),o=n(1e4),i=n(96770),s=n(98356),a=n(94248),u=n(35518),c=n(16967),l=n(27890),d=n(68732),f=n(91725),p=n(5173),h=n(86454),m=n(51375),g=n(38799),x=n(4103),v=n(81253),b=n(92950),y=n(53298),w=n(49186),j=n(67805),Z=n(40013),C=n(3217),k=n(87351),E=n(57548),N=n(51296),M=n(82929),O=n(10355),S=n(88239),_=n(36108),R=n(71550),L=n(72361),A=n(89939),V=n(10887),P=n(19367),H=n(322),D=n(89828),$=n(9027),z=n(92454),F=n(38057),q=n(34195),I=n(74992),T=n(74020),G=n(35601),Q=n(36263),K=n(52484),W=n(62125),B=n(96888),U=n(71001),Y=n(95255),J=n(57287),X=n(90412),tt=n(32938),te=n(69770),tn=n(67026),tr=n(6180),to=n(34390),ti=n(72469),ts=n(77227),ta=n(51809),tu=n(96689),tc=n(27154),tl=n(17933),td=n(7038),tf=n(96419),tp=n(67323),th=n(27478),tm=n(40651),tg=n(29538),tx=n(16691),tv=n.n(tx);function tb(t){return(0,r.jsx)(tv(),{alt:"Whombat Logo",src:"/whombat.svg",...t})}function ty(t){return(0,r.jsxs)("svg",{...t,viewBox:"-1.6 -1.6 19.20 19.20",xmlns:"http://www.w3.org/2000/svg",fill:"currentColor",transform:"rotate(0)matrix(1, 0, 0, 1, 0, 0)",stroke:"currentColor",strokeWidth:"0.16",children:[(0,r.jsx)("g",{id:"SVGRepo_bgCarrier",strokeWidth:"0"}),(0,r.jsx)("g",{id:"SVGRepo_tracerCarrier",strokeLinecap:"round",strokeLinejoin:"round"}),(0,r.jsxs)("g",{id:"SVGRepo_iconCarrier",children:[" ",(0,r.jsx)("path",{d:"M5 2V0H0v5h2v6H0v5h5v-2h6v2h5v-5h-2V5h2V0h-5v2H5zm6 1v2h2v6h-2v2H5v-2H3V5h2V3h6zm1-2h3v3h-3V1zm3 11v3h-3v-3h3zM4 15H1v-3h3v3zM1 4V1h3v3H1z"})," "]})]})}function tw(t){return(0,r.jsxs)("svg",{...t,viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg",transform:"rotate(90)",children:[(0,r.jsx)("g",{id:"SVGRepo_bgCarrier",strokeWidth:"0"}),(0,r.jsx)("g",{id:"SVGRepo_tracerCarrier",strokeLinecap:"round",strokeLinejoin:"round"}),(0,r.jsxs)("g",{id:"SVGRepo_iconCarrier",children:[" ",(0,r.jsx)("path",{d:"M12 18L12 6M12 18L9 16M12 18L15 16M12 6L9 8M12 6L15 8M21 3H3M21 21H3",stroke:"currentColor",strokeWidth:"1.5",strokeLinecap:"round",strokeLinejoin:"round"})," "]})]})}function tj(t){return(0,r.jsxs)("svg",{...t,stroke:"currentColor",viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,r.jsx)("g",{id:"SVGRepo_bgCarrier",strokeWidth:"0"}),(0,r.jsx)("g",{id:"SVGRepo_tracerCarrier",strokeLinecap:"round",strokeLinejoin:"round"}),(0,r.jsxs)("g",{id:"SVGRepo_iconCarrier",children:[" ",(0,r.jsxs)("g",{id:"Interface / Line_Xl",children:[" ",(0,r.jsx)("path",{id:"Vector",d:"M12 21V3",stroke:"currentColor",strokeWidth:"1.5",strokeLinecap:"round",strokeLinejoin:"round"})," "]})," "]})]})}function tZ(t){return(0,r.jsx)("svg",{...t,viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:(0,r.jsx)("g",{id:"Edit / Path",children:(0,r.jsx)("path",{id:"Vector",d:"M8.12132 15.8787C7.57843 15.3358 6.82843 15 6 15C4.34315 15 3 16.3431 3 18C3 19.6569 4.34315 21 6 21C7.65685 21 9 19.6569 9 18C9 17.1716 8.66421 16.4216 8.12132 15.8787ZM8.12132 15.8787L15.8787 8.12132M15.8787 8.12132C16.4216 8.66421 17.1716 9 18 9C19.6569 9 21 7.65685 21 6C21 4.34315 19.6569 3 18 3C16.3431 3 15 4.34315 15 6C15 6.82843 15.3358 7.57843 15.8787 8.12132ZM15.8787 8.12132L15.8828 8.11719",stroke:"currentColor","stroke-width":"1.5","stroke-linecap":"round","stroke-linejoin":"round"})})})}},17968:function(t,e,n){"use strict";n.d(e,{Z:function(){return a}});var r=n(23588),o=n(2265),i=n(81698),s=n(41095);function a(t){let{uuid:e,annotationProject:n,onUpdate:a,onDelete:u,onAddTag:c,onRemoveTag:l,onAddAnnotationTasks:d,onError:f,enabled:p=!0}=t,{query:h,useMutation:m,client:g}=(0,s.ZP)({uuid:e,initial:n,name:"annotation_project",enabled:p,getFn:i.Z.annotationProjects.get,onError:f}),x=m({mutationFn:i.Z.annotationProjects.update,onSuccess:a}),v=m({mutationFn:i.Z.annotationProjects.addTag,onSuccess:c}),b=m({mutationFn:i.Z.annotationProjects.removeTag,onSuccess:l}),y=m({mutationFn:i.Z.annotationProjects.delete,onSuccess:u}),{data:w}=h,j=(0,o.useCallback)(async t=>{if(null==w)return;let e=await i.Z.clips.createMany(t);return await i.Z.annotationTasks.createMany(w,e)},[w]),Z=(0,r.D)({mutationFn:j,onSuccess:t=>{null!=t&&(null==d||d(t),g.invalidateQueries({queryKey:["annotation_project",e]}))}}),C=(0,o.useMemo)(()=>{if(null!=w)return i.Z.annotationProjects.getDownloadUrl(w)},[w]);return{...h,update:x,addTag:v,addAnnotationTasks:Z,removeTag:b,delete:y,download:C}}},41095:function(t,e,n){"use strict";n.d(e,{ZP:function(){return a}});var r=n(23588),o=n(67663),i=n(38038),s=n(2265);function a(t){let{uuid:e,initial:n,name:a,enabled:u=!0,getFn:c,onError:l}=t,d=(0,i.NL)(),f=(0,s.useCallback)(async()=>{if(null==e)throw Error("No uuid provided for object of type ".concat(a));return await c(e)},[e,a,c]),p=(0,o.a)({queryKey:[a,e],queryFn:f,retry:(t,e)=>{var n;if(null==e)return t<3;let r=null==e?void 0:null===(n=e.response)||void 0===n?void 0:n.status;return null==r?t<3:(!(r>=400)||!(r<500))&&t<3},initialData:n,staleTime:3e5,enabled:u&&null!=e}),h=(0,s.useCallback)(t=>{d.setQueryData([a,e],t)},[d,e,a]),{error:m,isError:g}=p;return(0,s.useEffect)(()=>{g&&(null==l||l(m))},[m,g,l]),{query:p,client:d,setData:h,useQuery:t=>{let{queryFn:n,name:r,enabled:i=!1}=t;return function(t){let{uuid:e,query:n,queryFn:r,name:i,secondaryName:a,enabled:u=!1}=t,{status:c,data:l}=n,d=(0,s.useCallback)(async()=>{if("pending"===c)throw Error("No data for object of type ".concat(i," (uuid=").concat(e,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===c)throw Error("Error while loading object of type ".concat(i," (uuid=").concat(e,"), cannot mutate"));return await r(l)},[c,l,r,i,e]);return(0,o.a)({queryFn:d,queryKey:[i,e,a],enabled:"pending"!==c&&"error"!==c&&u})}({uuid:e,query:p,queryFn:n,secondaryName:r,name:a,enabled:i})},useMutation:t=>{let{mutationFn:n,onSuccess:o,onError:i,withUpdate:u=!0}=t;return function(t){let{uuid:e,query:n,client:o,mutationFn:i,name:a,onSuccess:u,onError:c,withUpdate:l=!0}=t,{status:d,data:f}=n,p=(0,s.useCallback)(async t=>{if(null==e)throw Error("No uuid provided for object of type ".concat(a));if("pending"===d)throw Error("No data for object of type ".concat(a," (uuid=").concat(e,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===d)throw Error("Error while loading object of type ".concat(a," (uuid=").concat(e,"), cannot mutate"));return await i(f,t)},[d,f,i,a,e]);return(0,r.D)({mutationFn:p,onSuccess:t=>{l&&o.setQueryData([a,e],t),null==u||u(t)},onError:c})}({uuid:e,query:p,client:d,mutationFn:n,name:a,onSuccess:o,onError:i,withUpdate:u})},useDestruction:t=>{let{mutationFn:n,onSuccess:o,onError:i}=t;return function(t){let{uuid:e,query:n,client:o,mutationFn:i,name:a,onSuccess:u,onError:c}=t,{status:l,data:d}=n,f=(0,s.useCallback)(async()=>{if(null==e)throw Error("No uuid provided for object of type ".concat(a));if("pending"===l)throw Error("No data for object of type ".concat(a," (uuid=").concat(e,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===l)throw Error("Error while loading object of type ".concat(a," (uuid=").concat(e,"), cannot mutate"));return await i(d)},[l,d,i,a,e]);return(0,r.D)({mutationFn:f,onSuccess:t=>{o.removeQueries({queryKey:[a,e]}),null==u||u(t)},onError:c})}({uuid:e,query:p,client:d,mutationFn:n,name:a,onSuccess:o,onError:i})}}}},61396:function(t,e,n){t.exports=n(25250)},24033:function(t,e,n){t.exports=n(15313)},23588:function(t,e,n){"use strict";n.d(e,{D:function(){return d}});var r=n(2265),o=n(77470),i=n(17987),s=n(42996),a=n(40300),u=class extends s.l{constructor(t,e){super(),this.#t=void 0,this.#e=t,this.setOptions(e),this.bindMethods(),this.#n()}#e;#t;#r;#o;bindMethods(){this.mutate=this.mutate.bind(this),this.reset=this.reset.bind(this)}setOptions(t){let e=this.options;this.options=this.#e.defaultMutationOptions(t),(0,a.VS)(e,this.options)||this.#e.getMutationCache().notify({type:"observerOptionsUpdated",mutation:this.#r,observer:this}),this.#r?.setOptions(this.options),e?.mutationKey&&this.options.mutationKey&&(0,a.Ym)(e.mutationKey)!==(0,a.Ym)(this.options.mutationKey)&&this.reset()}onUnsubscribe(){this.hasListeners()||this.#r?.removeObserver(this)}onMutationUpdate(t){this.#n(),this.#i(t)}getCurrentResult(){return this.#t}reset(){this.#r?.removeObserver(this),this.#r=void 0,this.#n(),this.#i()}mutate(t,e){return this.#o=e,this.#r?.removeObserver(this),this.#r=this.#e.getMutationCache().build(this.#e,this.options),this.#r.addObserver(this),this.#r.execute(t)}#n(){let t=this.#r?.state??(0,o.R)();this.#t={...t,isPending:"pending"===t.status,isSuccess:"success"===t.status,isError:"error"===t.status,isIdle:"idle"===t.status,mutate:this.mutate,reset:this.reset}}#i(t){i.V.batch(()=>{this.#o&&this.hasListeners()&&(t?.type==="success"?(this.#o.onSuccess?.(t.data,this.#t.variables,this.#t.context),this.#o.onSettled?.(t.data,null,this.#t.variables,this.#t.context)):t?.type==="error"&&(this.#o.onError?.(t.error,this.#t.variables,this.#t.context),this.#o.onSettled?.(void 0,t.error,this.#t.variables,this.#t.context))),this.listeners.forEach(t=>{t(this.#t)})})}},c=n(38038),l=n(14805);function d(t,e){let n=(0,c.NL)(e),[o]=r.useState(()=>new u(n,t));r.useEffect(()=>{o.setOptions(t)},[o,t]);let s=r.useSyncExternalStore(r.useCallback(t=>o.subscribe(i.V.batchCalls(t)),[o]),()=>o.getCurrentResult(),()=>o.getCurrentResult()),a=r.useCallback((t,e)=>{o.mutate(t,e).catch(f)},[o]);if(s.error&&(0,l.L)(o.options.throwOnError,[s.error]))throw s.error;return{...s,mutate:a,mutateAsync:s.mutate}}function f(){}},5925:function(t,e,n){"use strict";let r,o;n.d(e,{Ih:function(){return te},x7:function(){return td},ZP:function(){return tf},GK:function(){return C},Am:function(){return D}});var i,s=n(2265);let a={data:""},u=t=>"object"==typeof window?((t?t.querySelector("#_goober"):window._goober)||Object.assign((t||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:t||a,c=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,l=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,f=(t,e)=>{let n="",r="",o="";for(let i in t){let s=t[i];"@"==i[0]?"i"==i[1]?n=i+" "+s+";":r+="f"==i[1]?f(s,i):i+"{"+f(s,"k"==i[1]?"":e)+"}":"object"==typeof s?r+=f(s,e?e.replace(/([^,])+/g,t=>i.replace(/(^:.*)|([^,])+/g,e=>/&/.test(e)?e.replace(/&/g,t):t?t+" "+e:e)):i):null!=s&&(i=/^--/.test(i)?i:i.replace(/[A-Z]/g,"-$&").toLowerCase(),o+=f.p?f.p(i,s):i+":"+s+";")}return n+(e&&o?e+"{"+o+"}":o)+r},p={},h=t=>{if("object"==typeof t){let e="";for(let n in t)e+=n+h(t[n]);return e}return t},m=(t,e,n,r,o)=>{var i;let s=h(t),a=p[s]||(p[s]=(t=>{let e=0,n=11;for(;e<t.length;)n=101*n+t.charCodeAt(e++)>>>0;return"go"+n})(s));if(!p[a]){let e=s!==t?t:(t=>{let e,n,r=[{}];for(;e=c.exec(t.replace(l,""));)e[4]?r.shift():e[3]?(n=e[3].replace(d," ").trim(),r.unshift(r[0][n]=r[0][n]||{})):r[0][e[1]]=e[2].replace(d," ").trim();return r[0]})(t);p[a]=f(o?{["@keyframes "+a]:e}:e,n?"":"."+a)}let u=n&&p.g?p.g:null;return n&&(p.g=p[a]),i=p[a],u?e.data=e.data.replace(u,i):-1===e.data.indexOf(i)&&(e.data=r?i+e.data:e.data+i),a},g=(t,e,n)=>t.reduce((t,r,o)=>{let i=e[o];if(i&&i.call){let t=i(n),e=t&&t.props&&t.props.className||/^go/.test(t)&&t;i=e?"."+e:t&&"object"==typeof t?t.props?"":f(t,""):!1===t?"":t}return t+r+(null==i?"":i)},"");function x(t){let e=this||{},n=t.call?t(e.p):t;return m(n.unshift?n.raw?g(n,[].slice.call(arguments,1),e.p):n.reduce((t,n)=>Object.assign(t,n&&n.call?n(e.p):n),{}):n,u(e.target),e.g,e.o,e.k)}x.bind({g:1});let v,b,y,w=x.bind({k:1});function j(t,e){let n=this||{};return function(){let r=arguments;function o(i,s){let a=Object.assign({},i),u=a.className||o.className;n.p=Object.assign({theme:b&&b()},a),n.o=/ *go\d+/.test(u),a.className=x.apply(n,r)+(u?" "+u:""),e&&(a.ref=s);let c=t;return t[0]&&(c=a.as||t,delete a.as),y&&c[0]&&y(a),v(c,a)}return e?e(o):o}}var Z=t=>"function"==typeof t,C=(t,e)=>Z(t)?t(e):t,k=(r=0,()=>(++r).toString()),E=()=>{if(void 0===o&&"u">typeof window){let t=matchMedia("(prefers-reduced-motion: reduce)");o=!t||t.matches}return o},N=new Map,M=t=>{if(N.has(t))return;let e=setTimeout(()=>{N.delete(t),L({type:4,toastId:t})},1e3);N.set(t,e)},O=t=>{let e=N.get(t);e&&clearTimeout(e)},S=(t,e)=>{switch(e.type){case 0:return{...t,toasts:[e.toast,...t.toasts].slice(0,20)};case 1:return e.toast.id&&O(e.toast.id),{...t,toasts:t.toasts.map(t=>t.id===e.toast.id?{...t,...e.toast}:t)};case 2:let{toast:n}=e;return t.toasts.find(t=>t.id===n.id)?S(t,{type:1,toast:n}):S(t,{type:0,toast:n});case 3:let{toastId:r}=e;return r?M(r):t.toasts.forEach(t=>{M(t.id)}),{...t,toasts:t.toasts.map(t=>t.id===r||void 0===r?{...t,visible:!1}:t)};case 4:return void 0===e.toastId?{...t,toasts:[]}:{...t,toasts:t.toasts.filter(t=>t.id!==e.toastId)};case 5:return{...t,pausedAt:e.time};case 6:let o=e.time-(t.pausedAt||0);return{...t,pausedAt:void 0,toasts:t.toasts.map(t=>({...t,pauseDuration:t.pauseDuration+o}))}}},_=[],R={toasts:[],pausedAt:void 0},L=t=>{R=S(R,t),_.forEach(t=>{t(R)})},A={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},V=(t={})=>{let[e,n]=(0,s.useState)(R);(0,s.useEffect)(()=>(_.push(n),()=>{let t=_.indexOf(n);t>-1&&_.splice(t,1)}),[e]);let r=e.toasts.map(e=>{var n,r;return{...t,...t[e.type],...e,duration:e.duration||(null==(n=t[e.type])?void 0:n.duration)||(null==t?void 0:t.duration)||A[e.type],style:{...t.style,...null==(r=t[e.type])?void 0:r.style,...e.style}}});return{...e,toasts:r}},P=(t,e="blank",n)=>({createdAt:Date.now(),visible:!0,type:e,ariaProps:{role:"status","aria-live":"polite"},message:t,pauseDuration:0,...n,id:(null==n?void 0:n.id)||k()}),H=t=>(e,n)=>{let r=P(e,t,n);return L({type:2,toast:r}),r.id},D=(t,e)=>H("blank")(t,e);D.error=H("error"),D.success=H("success"),D.loading=H("loading"),D.custom=H("custom"),D.dismiss=t=>{L({type:3,toastId:t})},D.remove=t=>L({type:4,toastId:t}),D.promise=(t,e,n)=>{let r=D.loading(e.loading,{...n,...null==n?void 0:n.loading});return t.then(t=>(D.success(C(e.success,t),{id:r,...n,...null==n?void 0:n.success}),t)).catch(t=>{D.error(C(e.error,t),{id:r,...n,...null==n?void 0:n.error})}),t};var $=(t,e)=>{L({type:1,toast:{id:t,height:e}})},z=()=>{L({type:5,time:Date.now()})},F=t=>{let{toasts:e,pausedAt:n}=V(t);(0,s.useEffect)(()=>{if(n)return;let t=Date.now(),r=e.map(e=>{if(e.duration===1/0)return;let n=(e.duration||0)+e.pauseDuration-(t-e.createdAt);if(n<0){e.visible&&D.dismiss(e.id);return}return setTimeout(()=>D.dismiss(e.id),n)});return()=>{r.forEach(t=>t&&clearTimeout(t))}},[e,n]);let r=(0,s.useCallback)(()=>{n&&L({type:6,time:Date.now()})},[n]),o=(0,s.useCallback)((t,n)=>{let{reverseOrder:r=!1,gutter:o=8,defaultPosition:i}=n||{},s=e.filter(e=>(e.position||i)===(t.position||i)&&e.height),a=s.findIndex(e=>e.id===t.id),u=s.filter((t,e)=>e<a&&t.visible).length;return s.filter(t=>t.visible).slice(...r?[u+1]:[0,u]).reduce((t,e)=>t+(e.height||0)+o,0)},[e]);return{toasts:e,handlers:{updateHeight:$,startPause:z,endPause:r,calculateOffset:o}}},q=w`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,I=w`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,T=w`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,G=j("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${t=>t.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${q} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${I} 0.15s ease-out forwards;
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
    animation: ${T} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,Q=w`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,K=j("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${t=>t.secondary||"#e0e0e0"};
  border-right-color: ${t=>t.primary||"#616161"};
  animation: ${Q} 1s linear infinite;
`,W=w`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,B=w`
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
}`,U=j("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${t=>t.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${W} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${B} 0.2s ease-out forwards;
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
`,Y=j("div")`
  position: absolute;
`,J=j("div")`
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
`,te=({toast:t})=>{let{icon:e,type:n,iconTheme:r}=t;return void 0!==e?"string"==typeof e?s.createElement(tt,null,e):e:"blank"===n?null:s.createElement(J,null,s.createElement(K,{...r}),"loading"!==n&&s.createElement(Y,null,"error"===n?s.createElement(G,{...r}):s.createElement(U,{...r})))},tn=t=>`
0% {transform: translate3d(0,${-200*t}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,tr=t=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*t}%,-1px) scale(.6); opacity:0;}
`,to=j("div")`
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
`,ti=j("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,ts=(t,e)=>{let n=t.includes("top")?1:-1,[r,o]=E()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[tn(n),tr(n)];return{animation:e?`${w(r)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${w(o)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},ta=s.memo(({toast:t,position:e,style:n,children:r})=>{let o=t.height?ts(t.position||e||"top-center",t.visible):{opacity:0},i=s.createElement(te,{toast:t}),a=s.createElement(ti,{...t.ariaProps},C(t.message,t));return s.createElement(to,{className:t.className,style:{...o,...n,...t.style}},"function"==typeof r?r({icon:i,message:a}):s.createElement(s.Fragment,null,i,a))});i=s.createElement,f.p=void 0,v=i,b=void 0,y=void 0;var tu=({id:t,className:e,style:n,onHeightUpdate:r,children:o})=>{let i=s.useCallback(e=>{if(e){let n=()=>{r(t,e.getBoundingClientRect().height)};n(),new MutationObserver(n).observe(e,{subtree:!0,childList:!0,characterData:!0})}},[t,r]);return s.createElement("div",{ref:i,className:e,style:n},o)},tc=(t,e)=>{let n=t.includes("top"),r=t.includes("center")?{justifyContent:"center"}:t.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:E()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${e*(n?1:-1)}px)`,...n?{top:0}:{bottom:0},...r}},tl=x`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,td=({reverseOrder:t,position:e="top-center",toastOptions:n,gutter:r,children:o,containerStyle:i,containerClassName:a})=>{let{toasts:u,handlers:c}=F(n);return s.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...i},className:a,onMouseEnter:c.startPause,onMouseLeave:c.endPause},u.map(n=>{let i=n.position||e,a=tc(i,c.calculateOffset(n,{reverseOrder:t,gutter:r,defaultPosition:e}));return s.createElement(tu,{id:n.id,key:n.id,onHeightUpdate:c.updateHeight,className:n.visible?tl:"",style:a},"custom"===n.type?C(n.message,n):o?o(n):s.createElement(ta,{toast:n,position:i}))}))},tf=D}},function(t){t.O(0,[1749,9966,3475,8966,5250,7663,1698,2971,4938,1744],function(){return t(t.s=54598)}),_N_E=t.O()}]);