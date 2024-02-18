(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[9769],{61396:function(e,t,r){e.exports=r(25250)},24033:function(e,t,r){e.exports=r(15313)},66169:function(e,t,r){"use strict";r.d(t,{S1:function(){return a},ZT:function(){return n},jU:function(){return i},on:function(){return o}});var n=function(){};function o(e){for(var t=[],r=1;r<arguments.length;r++)t[r-1]=arguments[r];e&&e.addEventListener&&e.addEventListener.apply(e,t)}function a(e){for(var t=[],r=1;r<arguments.length;r++)t[r-1]=arguments[r];e&&e.removeEventListener&&e.removeEventListener.apply(e,t)}var i="undefined"!=typeof window},86063:function(e,t,r){"use strict";var n=r(2265),o=r(66169),a=n.useState;t.Z=function(e){var t,r,i=a(!1),s=i[0],u=i[1];return"function"==typeof e&&(e=e(s)),[n.cloneElement(e,{onMouseEnter:(t=e.props.onMouseEnter,function(e){(t||o.ZT)(e),u(!0)}),onMouseLeave:(r=e.props.onMouseLeave,function(e){(r||o.ZT)(e),u(!1)})}),s]}},58459:function(e,t,r){"use strict";r.d(t,{v:function(){return _}});var n,o,a,i=r(2265),s=r(60597),u=r(11931),l=r(85390),c=r(82769),d=r(32600),p=r(46618),f=r(75606),m=r(93850),v=r(53891),h=r(35863),y=r(65410),b=r(90583),g=r(50926),E=r(25306),x=r(8076),P=r(57728),I=r(12950),R=r(13995),S=r(19426),M=((n=M||{})[n.Open=0]="Open",n[n.Closed=1]="Closed",n),T=((o=T||{})[o.Pointer=0]="Pointer",o[o.Other=1]="Other",o),w=((a=w||{})[a.OpenMenu=0]="OpenMenu",a[a.CloseMenu=1]="CloseMenu",a[a.GoToItem=2]="GoToItem",a[a.Search=3]="Search",a[a.ClearSearch=4]="ClearSearch",a[a.RegisterItem=5]="RegisterItem",a[a.UnregisterItem=6]="UnregisterItem",a);function O(e,t=e=>e){let r=null!==e.activeItemIndex?e.items[e.activeItemIndex]:null,n=(0,y.z2)(t(e.items.slice()),e=>e.dataRef.current.domRef.current),o=r?n.indexOf(r):null;return -1===o&&(o=null),{items:n,activeItemIndex:o}}let k={1:e=>1===e.menuState?e:{...e,activeItemIndex:null,menuState:1},0:e=>0===e.menuState?e:{...e,__demoMode:!1,menuState:0},2:(e,t)=>{var r;let n=O(e),o=(0,v.d)(t,{resolveItems:()=>n.items,resolveActiveIndex:()=>n.activeItemIndex,resolveId:e=>e.id,resolveDisabled:e=>e.dataRef.current.disabled});return{...e,...n,searchQuery:"",activeItemIndex:o,activationTrigger:null!=(r=t.trigger)?r:1}},3:(e,t)=>{let r=""!==e.searchQuery?0:1,n=e.searchQuery+t.value.toLowerCase(),o=(null!==e.activeItemIndex?e.items.slice(e.activeItemIndex+r).concat(e.items.slice(0,e.activeItemIndex+r)):e.items).find(e=>{var t;return(null==(t=e.dataRef.current.textValue)?void 0:t.startsWith(n))&&!e.dataRef.current.disabled}),a=o?e.items.indexOf(o):-1;return -1===a||a===e.activeItemIndex?{...e,searchQuery:n}:{...e,searchQuery:n,activeItemIndex:a,activationTrigger:1}},4:e=>""===e.searchQuery?e:{...e,searchQuery:"",searchActiveItemIndex:null},5:(e,t)=>{let r=O(e,e=>[...e,{id:t.id,dataRef:t.dataRef}]);return{...e,...r}},6:(e,t)=>{let r=O(e,e=>{let r=e.findIndex(e=>e.id===t.id);return -1!==r&&e.splice(r,1),e});return{...e,...r,activationTrigger:1}}},C=(0,i.createContext)(null);function N(e){let t=(0,i.useContext)(C);if(null===t){let t=Error(`<${e} /> is missing a parent <Menu /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(t,N),t}return t}function D(e,t){return(0,s.E)(t.type,k,e,t)}C.displayName="MenuContext";let F=i.Fragment,A=u.AN.RenderStrategy|u.AN.Static,z=i.Fragment,_=Object.assign((0,u.yV)(function(e,t){let{__demoMode:r=!1,...n}=e,o=(0,i.useReducer)(D,{__demoMode:r,menuState:r?0:1,buttonRef:(0,i.createRef)(),itemsRef:(0,i.createRef)(),items:[],searchQuery:"",activeItemIndex:null,activationTrigger:1}),[{menuState:a,itemsRef:l,buttonRef:c},d]=o,f=(0,p.T)(t);(0,b.O)([c,l],(e,t)=>{var r;d({type:1}),(0,y.sP)(t,y.tJ.Loose)||(e.preventDefault(),null==(r=c.current)||r.focus())},0===a);let m=(0,I.z)(()=>{d({type:1})}),v=(0,i.useMemo)(()=>({open:0===a,close:m}),[a,m]);return i.createElement(C.Provider,{value:o},i.createElement(E.up,{value:(0,s.E)(a,{0:E.ZM.Open,1:E.ZM.Closed})},(0,u.sY)({ourProps:{ref:f},theirProps:n,slot:v,defaultTag:F,name:"Menu"})))}),{Button:(0,u.yV)(function(e,t){var r;let n=(0,f.M)(),{id:o=`headlessui-menu-button-${n}`,...a}=e,[s,l]=N("Menu.Button"),d=(0,p.T)(s.buttonRef,t),y=(0,c.G)(),b=(0,I.z)(e=>{switch(e.key){case m.R.Space:case m.R.Enter:case m.R.ArrowDown:e.preventDefault(),e.stopPropagation(),l({type:0}),y.nextFrame(()=>l({type:2,focus:v.T.First}));break;case m.R.ArrowUp:e.preventDefault(),e.stopPropagation(),l({type:0}),y.nextFrame(()=>l({type:2,focus:v.T.Last}))}}),g=(0,I.z)(e=>{e.key===m.R.Space&&e.preventDefault()}),E=(0,I.z)(t=>{if((0,h.P)(t.currentTarget))return t.preventDefault();e.disabled||(0===s.menuState?(l({type:1}),y.nextFrame(()=>{var e;return null==(e=s.buttonRef.current)?void 0:e.focus({preventScroll:!0})})):(t.preventDefault(),l({type:0})))}),P=(0,i.useMemo)(()=>({open:0===s.menuState}),[s]),R={ref:d,id:o,type:(0,x.f)(e,s.buttonRef),"aria-haspopup":"menu","aria-controls":null==(r=s.itemsRef.current)?void 0:r.id,"aria-expanded":0===s.menuState,onKeyDown:b,onKeyUp:g,onClick:E};return(0,u.sY)({ourProps:R,theirProps:a,slot:P,defaultTag:"button",name:"Menu.Button"})}),Items:(0,u.yV)(function(e,t){var r,n;let o=(0,f.M)(),{id:a=`headlessui-menu-items-${o}`,...s}=e,[d,h]=N("Menu.Items"),b=(0,p.T)(d.itemsRef,t),x=(0,P.i)(d.itemsRef),R=(0,c.G)(),S=(0,E.oJ)(),M=null!==S?(S&E.ZM.Open)===E.ZM.Open:0===d.menuState;(0,i.useEffect)(()=>{let e=d.itemsRef.current;e&&0===d.menuState&&e!==(null==x?void 0:x.activeElement)&&e.focus({preventScroll:!0})},[d.menuState,d.itemsRef,x]),(0,g.B)({container:d.itemsRef.current,enabled:0===d.menuState,accept:e=>"menuitem"===e.getAttribute("role")?NodeFilter.FILTER_REJECT:e.hasAttribute("role")?NodeFilter.FILTER_SKIP:NodeFilter.FILTER_ACCEPT,walk(e){e.setAttribute("role","none")}});let T=(0,I.z)(e=>{var t,r;switch(R.dispose(),e.key){case m.R.Space:if(""!==d.searchQuery)return e.preventDefault(),e.stopPropagation(),h({type:3,value:e.key});case m.R.Enter:if(e.preventDefault(),e.stopPropagation(),h({type:1}),null!==d.activeItemIndex){let{dataRef:e}=d.items[d.activeItemIndex];null==(r=null==(t=e.current)?void 0:t.domRef.current)||r.click()}(0,y.wI)(d.buttonRef.current);break;case m.R.ArrowDown:return e.preventDefault(),e.stopPropagation(),h({type:2,focus:v.T.Next});case m.R.ArrowUp:return e.preventDefault(),e.stopPropagation(),h({type:2,focus:v.T.Previous});case m.R.Home:case m.R.PageUp:return e.preventDefault(),e.stopPropagation(),h({type:2,focus:v.T.First});case m.R.End:case m.R.PageDown:return e.preventDefault(),e.stopPropagation(),h({type:2,focus:v.T.Last});case m.R.Escape:e.preventDefault(),e.stopPropagation(),h({type:1}),(0,l.k)().nextFrame(()=>{var e;return null==(e=d.buttonRef.current)?void 0:e.focus({preventScroll:!0})});break;case m.R.Tab:e.preventDefault(),e.stopPropagation(),h({type:1}),(0,l.k)().nextFrame(()=>{(0,y.EO)(d.buttonRef.current,e.shiftKey?y.TO.Previous:y.TO.Next)});break;default:1===e.key.length&&(h({type:3,value:e.key}),R.setTimeout(()=>h({type:4}),350))}}),w=(0,I.z)(e=>{e.key===m.R.Space&&e.preventDefault()}),O=(0,i.useMemo)(()=>({open:0===d.menuState}),[d]),k={"aria-activedescendant":null===d.activeItemIndex||null==(r=d.items[d.activeItemIndex])?void 0:r.id,"aria-labelledby":null==(n=d.buttonRef.current)?void 0:n.id,id:a,onKeyDown:T,onKeyUp:w,role:"menu",tabIndex:0,ref:b};return(0,u.sY)({ourProps:k,theirProps:s,slot:O,defaultTag:"div",features:A,visible:M,name:"Menu.Items"})}),Item:(0,u.yV)(function(e,t){let r=(0,f.M)(),{id:n=`headlessui-menu-item-${r}`,disabled:o=!1,...a}=e,[s,c]=N("Menu.Item"),m=null!==s.activeItemIndex&&s.items[s.activeItemIndex].id===n,h=(0,i.useRef)(null),b=(0,p.T)(t,h);(0,d.e)(()=>{if(s.__demoMode||0!==s.menuState||!m||0===s.activationTrigger)return;let e=(0,l.k)();return e.requestAnimationFrame(()=>{var e,t;null==(t=null==(e=h.current)?void 0:e.scrollIntoView)||t.call(e,{block:"nearest"})}),e.dispose},[s.__demoMode,h,m,s.menuState,s.activationTrigger,s.activeItemIndex]);let g=(0,S.x)(h),E=(0,i.useRef)({disabled:o,domRef:h,get textValue(){return g()}});(0,d.e)(()=>{E.current.disabled=o},[E,o]),(0,d.e)(()=>(c({type:5,id:n,dataRef:E}),()=>c({type:6,id:n})),[E,n]);let x=(0,I.z)(()=>{c({type:1})}),P=(0,I.z)(e=>{if(o)return e.preventDefault();c({type:1}),(0,y.wI)(s.buttonRef.current)}),M=(0,I.z)(()=>{if(o)return c({type:2,focus:v.T.Nothing});c({type:2,focus:v.T.Specific,id:n})}),T=(0,R.g)(),w=(0,I.z)(e=>T.update(e)),O=(0,I.z)(e=>{T.wasMoved(e)&&(o||m||c({type:2,focus:v.T.Specific,id:n,trigger:0}))}),k=(0,I.z)(e=>{T.wasMoved(e)&&(o||m&&c({type:2,focus:v.T.Nothing}))}),C=(0,i.useMemo)(()=>({active:m,disabled:o,close:x}),[m,o,x]);return(0,u.sY)({ourProps:{id:n,ref:b,role:"menuitem",tabIndex:!0===o?void 0:-1,"aria-disabled":!0===o||void 0,disabled:void 0,onClick:P,onFocus:M,onPointerEnter:w,onMouseEnter:w,onPointerMove:O,onMouseMove:O,onPointerLeave:k,onMouseLeave:k},theirProps:a,slot:C,defaultTag:z,name:"Menu.Item"})})})},73999:function(e,t,r){"use strict";r.d(t,{J:function(){return $}});var n,o,a=r(2265),i=r(60597),s=r(11931),u=r(46618),l=r(75606),c=r(93850),d=r(35863),p=r(65410),f=r(25306),m=r(8076),v=r(90583),h=r(54851),y=r(57728),b=r(6890),g=r(58227),E=r(12950),x=r(49376),P=r(61858),I=r(32600),R=r(59985),S=r(87250),M=((n=M||{})[n.Open=0]="Open",n[n.Closed=1]="Closed",n),T=((o=T||{})[o.TogglePopover=0]="TogglePopover",o[o.ClosePopover=1]="ClosePopover",o[o.SetButton=2]="SetButton",o[o.SetButtonId=3]="SetButtonId",o[o.SetPanel=4]="SetPanel",o[o.SetPanelId=5]="SetPanelId",o);let w={0:e=>{let t={...e,popoverState:(0,i.E)(e.popoverState,{0:1,1:0})};return 0===t.popoverState&&(t.__demoMode=!1),t},1:e=>1===e.popoverState?e:{...e,popoverState:1},2:(e,t)=>e.button===t.button?e:{...e,button:t.button},3:(e,t)=>e.buttonId===t.buttonId?e:{...e,buttonId:t.buttonId},4:(e,t)=>e.panel===t.panel?e:{...e,panel:t.panel},5:(e,t)=>e.panelId===t.panelId?e:{...e,panelId:t.panelId}},O=(0,a.createContext)(null);function k(e){let t=(0,a.useContext)(O);if(null===t){let t=Error(`<${e} /> is missing a parent <Popover /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(t,k),t}return t}O.displayName="PopoverContext";let C=(0,a.createContext)(null);function N(e){let t=(0,a.useContext)(C);if(null===t){let t=Error(`<${e} /> is missing a parent <Popover /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(t,N),t}return t}C.displayName="PopoverAPIContext";let D=(0,a.createContext)(null);function F(){return(0,a.useContext)(D)}D.displayName="PopoverGroupContext";let A=(0,a.createContext)(null);function z(e,t){return(0,i.E)(t.type,w,e,t)}A.displayName="PopoverPanelContext";let _=s.AN.RenderStrategy|s.AN.Static,L=s.AN.RenderStrategy|s.AN.Static,$=Object.assign((0,s.yV)(function(e,t){var r;let{__demoMode:n=!1,...o}=e,l=(0,a.useRef)(null),c=(0,u.T)(t,(0,u.h)(e=>{l.current=e})),d=(0,a.useRef)([]),m=(0,a.useReducer)(z,{__demoMode:n,popoverState:n?0:1,buttons:d,button:null,buttonId:null,panel:null,panelId:null,beforePanelSentinel:(0,a.createRef)(),afterPanelSentinel:(0,a.createRef)()}),[{popoverState:h,button:g,buttonId:x,panel:I,panelId:M,beforePanelSentinel:T,afterPanelSentinel:w},k]=m,N=(0,y.i)(null!=(r=l.current)?r:g),D=(0,a.useMemo)(()=>{if(!g||!I)return!1;for(let e of document.querySelectorAll("body > *"))if(Number(null==e?void 0:e.contains(g))^Number(null==e?void 0:e.contains(I)))return!0;let e=(0,p.GO)(),t=e.indexOf(g),r=(t+e.length-1)%e.length,n=(t+1)%e.length,o=e[r],a=e[n];return!I.contains(o)&&!I.contains(a)},[g,I]),_=(0,P.E)(x),L=(0,P.E)(M),$=(0,a.useMemo)(()=>({buttonId:_,panelId:L,close:()=>k({type:1})}),[_,L,k]),B=F(),j=null==B?void 0:B.registerPopover,H=(0,E.z)(()=>{var e;return null!=(e=null==B?void 0:B.isFocusWithinPopoverGroup())?e:(null==N?void 0:N.activeElement)&&((null==g?void 0:g.contains(N.activeElement))||(null==I?void 0:I.contains(N.activeElement)))});(0,a.useEffect)(()=>null==j?void 0:j($),[j,$]);let[K,V]=(0,S.k)(),Z=(0,R.v)({mainTreeNodeRef:null==B?void 0:B.mainTreeNodeRef,portals:K,defaultContainers:[g,I]});(0,b.O)(null==N?void 0:N.defaultView,"focus",e=>{var t,r,n,o;e.target!==window&&e.target instanceof HTMLElement&&0===h&&(H()||g&&I&&(Z.contains(e.target)||null!=(r=null==(t=T.current)?void 0:t.contains)&&r.call(t,e.target)||null!=(o=null==(n=w.current)?void 0:n.contains)&&o.call(n,e.target)||k({type:1})))},!0),(0,v.O)(Z.resolveContainers,(e,t)=>{k({type:1}),(0,p.sP)(t,p.tJ.Loose)||(e.preventDefault(),null==g||g.focus())},0===h);let G=(0,E.z)(e=>{k({type:1});let t=e?e instanceof HTMLElement?e:"current"in e&&e.current instanceof HTMLElement?e.current:g:g;null==t||t.focus()}),U=(0,a.useMemo)(()=>({close:G,isPortalled:D}),[G,D]),Y=(0,a.useMemo)(()=>({open:0===h,close:G}),[h,G]);return a.createElement(A.Provider,{value:null},a.createElement(O.Provider,{value:m},a.createElement(C.Provider,{value:U},a.createElement(f.up,{value:(0,i.E)(h,{0:f.ZM.Open,1:f.ZM.Closed})},a.createElement(V,null,(0,s.sY)({ourProps:{ref:c},theirProps:o,slot:Y,defaultTag:"div",name:"Popover"}),a.createElement(Z.MainTreeNode,null))))))}),{Button:(0,s.yV)(function(e,t){let r=(0,l.M)(),{id:n=`headlessui-popover-button-${r}`,...o}=e,[f,v]=k("Popover.Button"),{isPortalled:h}=N("Popover.Button"),b=(0,a.useRef)(null),P=`headlessui-focus-sentinel-${(0,l.M)()}`,I=F(),R=null==I?void 0:I.closeOthers,S=null!==(0,a.useContext)(A);(0,a.useEffect)(()=>{if(!S)return v({type:3,buttonId:n}),()=>{v({type:3,buttonId:null})}},[S,n,v]);let[M]=(0,a.useState)(()=>Symbol()),T=(0,u.T)(b,t,S?null:e=>{if(e)f.buttons.current.push(M);else{let e=f.buttons.current.indexOf(M);-1!==e&&f.buttons.current.splice(e,1)}f.buttons.current.length>1&&console.warn("You are already using a <Popover.Button /> but only 1 <Popover.Button /> is supported."),e&&v({type:2,button:e})}),w=(0,u.T)(b,t),O=(0,y.i)(b),C=(0,E.z)(e=>{var t,r,n;if(S){if(1===f.popoverState)return;switch(e.key){case c.R.Space:case c.R.Enter:e.preventDefault(),null==(r=(t=e.target).click)||r.call(t),v({type:1}),null==(n=f.button)||n.focus()}}else switch(e.key){case c.R.Space:case c.R.Enter:e.preventDefault(),e.stopPropagation(),1===f.popoverState&&(null==R||R(f.buttonId)),v({type:0});break;case c.R.Escape:if(0!==f.popoverState)return null==R?void 0:R(f.buttonId);if(!b.current||null!=O&&O.activeElement&&!b.current.contains(O.activeElement))return;e.preventDefault(),e.stopPropagation(),v({type:1})}}),D=(0,E.z)(e=>{S||e.key===c.R.Space&&e.preventDefault()}),z=(0,E.z)(t=>{var r,n;(0,d.P)(t.currentTarget)||e.disabled||(S?(v({type:1}),null==(r=f.button)||r.focus()):(t.preventDefault(),t.stopPropagation(),1===f.popoverState&&(null==R||R(f.buttonId)),v({type:0}),null==(n=f.button)||n.focus()))}),_=(0,E.z)(e=>{e.preventDefault(),e.stopPropagation()}),L=0===f.popoverState,$=(0,a.useMemo)(()=>({open:L}),[L]),B=(0,m.f)(e,b),j=S?{ref:w,type:B,onKeyDown:C,onClick:z}:{ref:T,id:f.buttonId,type:B,"aria-expanded":0===f.popoverState,"aria-controls":f.panel?f.panelId:void 0,onKeyDown:C,onKeyUp:D,onClick:z,onMouseDown:_},H=(0,x.l)(),K=(0,E.z)(()=>{let e=f.panel;e&&(0,i.E)(H.current,{[x.N.Forwards]:()=>(0,p.jA)(e,p.TO.First),[x.N.Backwards]:()=>(0,p.jA)(e,p.TO.Last)})===p.fE.Error&&(0,p.jA)((0,p.GO)().filter(e=>"true"!==e.dataset.headlessuiFocusGuard),(0,i.E)(H.current,{[x.N.Forwards]:p.TO.Next,[x.N.Backwards]:p.TO.Previous}),{relativeTo:f.button})});return a.createElement(a.Fragment,null,(0,s.sY)({ourProps:j,theirProps:o,slot:$,defaultTag:"button",name:"Popover.Button"}),L&&!S&&h&&a.createElement(g._,{id:P,features:g.A.Focusable,"data-headlessui-focus-guard":!0,as:"button",type:"button",onFocus:K}))}),Overlay:(0,s.yV)(function(e,t){let r=(0,l.M)(),{id:n=`headlessui-popover-overlay-${r}`,...o}=e,[{popoverState:i},c]=k("Popover.Overlay"),p=(0,u.T)(t),m=(0,f.oJ)(),v=null!==m?(m&f.ZM.Open)===f.ZM.Open:0===i,h=(0,E.z)(e=>{if((0,d.P)(e.currentTarget))return e.preventDefault();c({type:1})}),y=(0,a.useMemo)(()=>({open:0===i}),[i]);return(0,s.sY)({ourProps:{ref:p,id:n,"aria-hidden":!0,onClick:h},theirProps:o,slot:y,defaultTag:"div",features:_,visible:v,name:"Popover.Overlay"})}),Panel:(0,s.yV)(function(e,t){let r=(0,l.M)(),{id:n=`headlessui-popover-panel-${r}`,focus:o=!1,...d}=e,[m,v]=k("Popover.Panel"),{close:h,isPortalled:b}=N("Popover.Panel"),P=`headlessui-focus-sentinel-before-${(0,l.M)()}`,R=`headlessui-focus-sentinel-after-${(0,l.M)()}`,S=(0,a.useRef)(null),M=(0,u.T)(S,t,e=>{v({type:4,panel:e})}),T=(0,y.i)(S);(0,I.e)(()=>(v({type:5,panelId:n}),()=>{v({type:5,panelId:null})}),[n,v]);let w=(0,f.oJ)(),O=null!==w?(w&f.ZM.Open)===f.ZM.Open:0===m.popoverState,C=(0,E.z)(e=>{var t;if(e.key===c.R.Escape){if(0!==m.popoverState||!S.current||null!=T&&T.activeElement&&!S.current.contains(T.activeElement))return;e.preventDefault(),e.stopPropagation(),v({type:1}),null==(t=m.button)||t.focus()}});(0,a.useEffect)(()=>{var t;e.static||1===m.popoverState&&(null==(t=e.unmount)||t)&&v({type:4,panel:null})},[m.popoverState,e.unmount,e.static,v]),(0,a.useEffect)(()=>{if(m.__demoMode||!o||0!==m.popoverState||!S.current)return;let e=null==T?void 0:T.activeElement;S.current.contains(e)||(0,p.jA)(S.current,p.TO.First)},[m.__demoMode,o,S,m.popoverState]);let D=(0,a.useMemo)(()=>({open:0===m.popoverState,close:h}),[m,h]),F={ref:M,id:n,onKeyDown:C,onBlur:o&&0===m.popoverState?e=>{var t,r,n,o,a;let i=e.relatedTarget;i&&S.current&&(null!=(t=S.current)&&t.contains(i)||(v({type:1}),(null!=(n=null==(r=m.beforePanelSentinel.current)?void 0:r.contains)&&n.call(r,i)||null!=(a=null==(o=m.afterPanelSentinel.current)?void 0:o.contains)&&a.call(o,i))&&i.focus({preventScroll:!0})))}:void 0,tabIndex:-1},z=(0,x.l)(),_=(0,E.z)(()=>{let e=S.current;e&&(0,i.E)(z.current,{[x.N.Forwards]:()=>{var t;(0,p.jA)(e,p.TO.First)===p.fE.Error&&(null==(t=m.afterPanelSentinel.current)||t.focus())},[x.N.Backwards]:()=>{var e;null==(e=m.button)||e.focus({preventScroll:!0})}})}),$=(0,E.z)(()=>{let e=S.current;e&&(0,i.E)(z.current,{[x.N.Forwards]:()=>{var e;if(!m.button)return;let t=(0,p.GO)(),r=t.indexOf(m.button),n=t.slice(0,r+1),o=[...t.slice(r+1),...n];for(let t of o.slice())if("true"===t.dataset.headlessuiFocusGuard||null!=(e=m.panel)&&e.contains(t)){let e=o.indexOf(t);-1!==e&&o.splice(e,1)}(0,p.jA)(o,p.TO.First,{sorted:!1})},[x.N.Backwards]:()=>{var t;(0,p.jA)(e,p.TO.Previous)===p.fE.Error&&(null==(t=m.button)||t.focus())}})});return a.createElement(A.Provider,{value:n},O&&b&&a.createElement(g._,{id:P,ref:m.beforePanelSentinel,features:g.A.Focusable,"data-headlessui-focus-guard":!0,as:"button",type:"button",onFocus:_}),(0,s.sY)({ourProps:F,theirProps:d,slot:D,defaultTag:"div",features:L,visible:O,name:"Popover.Panel"}),O&&b&&a.createElement(g._,{id:R,ref:m.afterPanelSentinel,features:g.A.Focusable,"data-headlessui-focus-guard":!0,as:"button",type:"button",onFocus:$}))}),Group:(0,s.yV)(function(e,t){let r=(0,a.useRef)(null),n=(0,u.T)(r,t),[o,i]=(0,a.useState)([]),l=(0,R.H)(),c=(0,E.z)(e=>{i(t=>{let r=t.indexOf(e);if(-1!==r){let e=t.slice();return e.splice(r,1),e}return t})}),d=(0,E.z)(e=>(i(t=>[...t,e]),()=>c(e))),p=(0,E.z)(()=>{var e;let t=(0,h.r)(r);if(!t)return!1;let n=t.activeElement;return!!(null!=(e=r.current)&&e.contains(n))||o.some(e=>{var r,o;return(null==(r=t.getElementById(e.buttonId.current))?void 0:r.contains(n))||(null==(o=t.getElementById(e.panelId.current))?void 0:o.contains(n))})}),f=(0,E.z)(e=>{for(let t of o)t.buttonId.current!==e&&t.close()}),m=(0,a.useMemo)(()=>({registerPopover:d,unregisterPopover:c,isFocusWithinPopoverGroup:p,closeOthers:f,mainTreeNodeRef:l.mainTreeNodeRef}),[d,c,p,f,l.mainTreeNodeRef]),v=(0,a.useMemo)(()=>({}),[]);return a.createElement(D.Provider,{value:m},(0,s.sY)({ourProps:{ref:n},theirProps:e,slot:v,defaultTag:"div",name:"Popover.Group"}),a.createElement(l.MainTreeNode,null))})})},6890:function(e,t,r){"use strict";r.d(t,{O:function(){return a}});var n=r(2265),o=r(61858);function a(e,t,r,a){let i=(0,o.E)(r);(0,n.useEffect)(()=>{function r(e){i.current(e)}return(e=null!=e?e:window).addEventListener(t,r,a),()=>e.removeEventListener(t,r,a)},[e,t,a])}},59985:function(e,t,r){"use strict";r.d(t,{H:function(){return u},v:function(){return s}});var n=r(2265),o=r(58227),a=r(12950),i=r(57728);function s({defaultContainers:e=[],portals:t,mainTreeNodeRef:r}={}){var s;let u=(0,n.useRef)(null!=(s=null==r?void 0:r.current)?s:null),l=(0,i.i)(u),c=(0,a.z)(()=>{var r;let n=[];for(let t of e)null!==t&&(t instanceof HTMLElement?n.push(t):"current"in t&&t.current instanceof HTMLElement&&n.push(t.current));if(null!=t&&t.current)for(let e of t.current)n.push(e);for(let e of null!=(r=null==l?void 0:l.querySelectorAll("html > *, body > *"))?r:[])e!==document.body&&e!==document.head&&e instanceof HTMLElement&&"headlessui-portal-root"!==e.id&&(e.contains(u.current)||n.some(t=>e.contains(t))||n.push(e));return n});return{resolveContainers:c,contains:(0,a.z)(e=>c().some(t=>t.contains(e))),mainTreeNodeRef:u,MainTreeNode:(0,n.useMemo)(()=>function(){return null!=r?null:n.createElement(o._,{features:o.A.Hidden,ref:u})},[u,r])}}function u(){let e=(0,n.useRef)(null);return{mainTreeNodeRef:e,MainTreeNode:(0,n.useMemo)(()=>function(){return n.createElement(o._,{features:o.A.Hidden,ref:e})},[e])}}},49376:function(e,t,r){"use strict";r.d(t,{N:function(){return i},l:function(){return s}});var n,o=r(2265),a=r(27976),i=((n=i||{})[n.Forwards=0]="Forwards",n[n.Backwards=1]="Backwards",n);function s(){let e=(0,o.useRef)(0);return(0,a.s)("keydown",t=>{"Tab"===t.key&&(e.current=t.shiftKey?1:0)},!0),e}},50926:function(e,t,r){"use strict";r.d(t,{B:function(){return i}});var n=r(2265),o=r(32600),a=r(54851);function i({container:e,accept:t,walk:r,enabled:i=!0}){let s=(0,n.useRef)(t),u=(0,n.useRef)(r);(0,n.useEffect)(()=>{s.current=t,u.current=r},[t,r]),(0,o.e)(()=>{if(!e||!i)return;let t=(0,a.r)(e);if(!t)return;let r=s.current,n=u.current,o=Object.assign(e=>r(e),{acceptNode:r}),l=t.createTreeWalker(e,NodeFilter.SHOW_ELEMENT,o,!1);for(;l.nextNode();)n(l.currentNode)},[e,i,s,u])}},23588:function(e,t,r){"use strict";r.d(t,{D:function(){return d}});var n=r(2265),o=r(77470),a=r(17987),i=r(42996),s=r(40300),u=class extends i.l{constructor(e,t){super(),this.#e=void 0,this.#t=e,this.setOptions(t),this.bindMethods(),this.#r()}#t;#e;#n;#o;bindMethods(){this.mutate=this.mutate.bind(this),this.reset=this.reset.bind(this)}setOptions(e){let t=this.options;this.options=this.#t.defaultMutationOptions(e),(0,s.VS)(t,this.options)||this.#t.getMutationCache().notify({type:"observerOptionsUpdated",mutation:this.#n,observer:this}),this.#n?.setOptions(this.options),t?.mutationKey&&this.options.mutationKey&&(0,s.Ym)(t.mutationKey)!==(0,s.Ym)(this.options.mutationKey)&&this.reset()}onUnsubscribe(){this.hasListeners()||this.#n?.removeObserver(this)}onMutationUpdate(e){this.#r(),this.#a(e)}getCurrentResult(){return this.#e}reset(){this.#n?.removeObserver(this),this.#n=void 0,this.#r(),this.#a()}mutate(e,t){return this.#o=t,this.#n?.removeObserver(this),this.#n=this.#t.getMutationCache().build(this.#t,this.options),this.#n.addObserver(this),this.#n.execute(e)}#r(){let e=this.#n?.state??(0,o.R)();this.#e={...e,isPending:"pending"===e.status,isSuccess:"success"===e.status,isError:"error"===e.status,isIdle:"idle"===e.status,mutate:this.mutate,reset:this.reset}}#a(e){a.V.batch(()=>{this.#o&&this.hasListeners()&&(e?.type==="success"?(this.#o.onSuccess?.(e.data,this.#e.variables,this.#e.context),this.#o.onSettled?.(e.data,null,this.#e.variables,this.#e.context)):e?.type==="error"&&(this.#o.onError?.(e.error,this.#e.variables,this.#e.context),this.#o.onSettled?.(void 0,e.error,this.#e.variables,this.#e.context))),this.listeners.forEach(e=>{e(this.#e)})})}},l=r(38038),c=r(14805);function d(e,t){let r=(0,l.NL)(t),[o]=n.useState(()=>new u(r,e));n.useEffect(()=>{o.setOptions(e)},[o,e]);let i=n.useSyncExternalStore(n.useCallback(e=>o.subscribe(a.V.batchCalls(e)),[o]),()=>o.getCurrentResult(),()=>o.getCurrentResult()),s=n.useCallback((e,t)=>{o.mutate(e,t).catch(p)},[o]);if(i.error&&(0,c.L)(o.options.throwOnError,[i.error]))throw i.error;return{...i,mutate:s,mutateAsync:i.mutate}}function p(){}},5925:function(e,t,r){"use strict";let n,o;r.d(t,{Ih:function(){return et},x7:function(){return ed},ZP:function(){return ep},GK:function(){return R},Am:function(){return L}});var a,i=r(2265);let s={data:""},u=e=>"object"==typeof window?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||s,l=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,c=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,p=(e,t)=>{let r="",n="",o="";for(let a in e){let i=e[a];"@"==a[0]?"i"==a[1]?r=a+" "+i+";":n+="f"==a[1]?p(i,a):a+"{"+p(i,"k"==a[1]?"":t)+"}":"object"==typeof i?n+=p(i,t?t.replace(/([^,])+/g,e=>a.replace(/(^:.*)|([^,])+/g,t=>/&/.test(t)?t.replace(/&/g,e):e?e+" "+t:t)):a):null!=i&&(a=/^--/.test(a)?a:a.replace(/[A-Z]/g,"-$&").toLowerCase(),o+=p.p?p.p(a,i):a+":"+i+";")}return r+(t&&o?t+"{"+o+"}":o)+n},f={},m=e=>{if("object"==typeof e){let t="";for(let r in e)t+=r+m(e[r]);return t}return e},v=(e,t,r,n,o)=>{var a;let i=m(e),s=f[i]||(f[i]=(e=>{let t=0,r=11;for(;t<e.length;)r=101*r+e.charCodeAt(t++)>>>0;return"go"+r})(i));if(!f[s]){let t=i!==e?e:(e=>{let t,r,n=[{}];for(;t=l.exec(e.replace(c,""));)t[4]?n.shift():t[3]?(r=t[3].replace(d," ").trim(),n.unshift(n[0][r]=n[0][r]||{})):n[0][t[1]]=t[2].replace(d," ").trim();return n[0]})(e);f[s]=p(o?{["@keyframes "+s]:t}:t,r?"":"."+s)}let u=r&&f.g?f.g:null;return r&&(f.g=f[s]),a=f[s],u?t.data=t.data.replace(u,a):-1===t.data.indexOf(a)&&(t.data=n?a+t.data:t.data+a),s},h=(e,t,r)=>e.reduce((e,n,o)=>{let a=t[o];if(a&&a.call){let e=a(r),t=e&&e.props&&e.props.className||/^go/.test(e)&&e;a=t?"."+t:e&&"object"==typeof e?e.props?"":p(e,""):!1===e?"":e}return e+n+(null==a?"":a)},"");function y(e){let t=this||{},r=e.call?e(t.p):e;return v(r.unshift?r.raw?h(r,[].slice.call(arguments,1),t.p):r.reduce((e,r)=>Object.assign(e,r&&r.call?r(t.p):r),{}):r,u(t.target),t.g,t.o,t.k)}y.bind({g:1});let b,g,E,x=y.bind({k:1});function P(e,t){let r=this||{};return function(){let n=arguments;function o(a,i){let s=Object.assign({},a),u=s.className||o.className;r.p=Object.assign({theme:g&&g()},s),r.o=/ *go\d+/.test(u),s.className=y.apply(r,n)+(u?" "+u:""),t&&(s.ref=i);let l=e;return e[0]&&(l=s.as||e,delete s.as),E&&l[0]&&E(s),b(l,s)}return t?t(o):o}}var I=e=>"function"==typeof e,R=(e,t)=>I(e)?e(t):e,S=(n=0,()=>(++n).toString()),M=()=>{if(void 0===o&&"u">typeof window){let e=matchMedia("(prefers-reduced-motion: reduce)");o=!e||e.matches}return o},T=new Map,w=e=>{if(T.has(e))return;let t=setTimeout(()=>{T.delete(e),D({type:4,toastId:e})},1e3);T.set(e,t)},O=e=>{let t=T.get(e);t&&clearTimeout(t)},k=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,20)};case 1:return t.toast.id&&O(t.toast.id),{...e,toasts:e.toasts.map(e=>e.id===t.toast.id?{...e,...t.toast}:e)};case 2:let{toast:r}=t;return e.toasts.find(e=>e.id===r.id)?k(e,{type:1,toast:r}):k(e,{type:0,toast:r});case 3:let{toastId:n}=t;return n?w(n):e.toasts.forEach(e=>{w(e.id)}),{...e,toasts:e.toasts.map(e=>e.id===n||void 0===n?{...e,visible:!1}:e)};case 4:return void 0===t.toastId?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(e=>e.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let o=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(e=>({...e,pauseDuration:e.pauseDuration+o}))}}},C=[],N={toasts:[],pausedAt:void 0},D=e=>{N=k(N,e),C.forEach(e=>{e(N)})},F={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},A=(e={})=>{let[t,r]=(0,i.useState)(N);(0,i.useEffect)(()=>(C.push(r),()=>{let e=C.indexOf(r);e>-1&&C.splice(e,1)}),[t]);let n=t.toasts.map(t=>{var r,n;return{...e,...e[t.type],...t,duration:t.duration||(null==(r=e[t.type])?void 0:r.duration)||(null==e?void 0:e.duration)||F[t.type],style:{...e.style,...null==(n=e[t.type])?void 0:n.style,...t.style}}});return{...t,toasts:n}},z=(e,t="blank",r)=>({createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...r,id:(null==r?void 0:r.id)||S()}),_=e=>(t,r)=>{let n=z(t,e,r);return D({type:2,toast:n}),n.id},L=(e,t)=>_("blank")(e,t);L.error=_("error"),L.success=_("success"),L.loading=_("loading"),L.custom=_("custom"),L.dismiss=e=>{D({type:3,toastId:e})},L.remove=e=>D({type:4,toastId:e}),L.promise=(e,t,r)=>{let n=L.loading(t.loading,{...r,...null==r?void 0:r.loading});return e.then(e=>(L.success(R(t.success,e),{id:n,...r,...null==r?void 0:r.success}),e)).catch(e=>{L.error(R(t.error,e),{id:n,...r,...null==r?void 0:r.error})}),e};var $=(e,t)=>{D({type:1,toast:{id:e,height:t}})},B=()=>{D({type:5,time:Date.now()})},j=e=>{let{toasts:t,pausedAt:r}=A(e);(0,i.useEffect)(()=>{if(r)return;let e=Date.now(),n=t.map(t=>{if(t.duration===1/0)return;let r=(t.duration||0)+t.pauseDuration-(e-t.createdAt);if(r<0){t.visible&&L.dismiss(t.id);return}return setTimeout(()=>L.dismiss(t.id),r)});return()=>{n.forEach(e=>e&&clearTimeout(e))}},[t,r]);let n=(0,i.useCallback)(()=>{r&&D({type:6,time:Date.now()})},[r]),o=(0,i.useCallback)((e,r)=>{let{reverseOrder:n=!1,gutter:o=8,defaultPosition:a}=r||{},i=t.filter(t=>(t.position||a)===(e.position||a)&&t.height),s=i.findIndex(t=>t.id===e.id),u=i.filter((e,t)=>t<s&&e.visible).length;return i.filter(e=>e.visible).slice(...n?[u+1]:[0,u]).reduce((e,t)=>e+(t.height||0)+o,0)},[t]);return{toasts:t,handlers:{updateHeight:$,startPause:B,endPause:n,calculateOffset:o}}},H=x`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,K=x`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,V=x`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,Z=P("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${H} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
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
    background: ${e=>e.secondary||"#fff"};
    bottom: 9px;
    left: 4px;
    height: 2px;
    width: 12px;
  }

  &:before {
    animation: ${V} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,G=x`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,U=P("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${G} 1s linear infinite;
`,Y=x`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,Q=x`
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
}`,J=P("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${Y} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${Q} 0.2s ease-out forwards;
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
`,W=P("div")`
  position: absolute;
`,q=P("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,X=x`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,ee=P("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${X} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,et=({toast:e})=>{let{icon:t,type:r,iconTheme:n}=e;return void 0!==t?"string"==typeof t?i.createElement(ee,null,t):t:"blank"===r?null:i.createElement(q,null,i.createElement(U,{...n}),"loading"!==r&&i.createElement(W,null,"error"===r?i.createElement(Z,{...n}):i.createElement(J,{...n})))},er=e=>`
0% {transform: translate3d(0,${-200*e}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,en=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*e}%,-1px) scale(.6); opacity:0;}
`,eo=P("div")`
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
`,ea=P("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,ei=(e,t)=>{let r=e.includes("top")?1:-1,[n,o]=M()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[er(r),en(r)];return{animation:t?`${x(n)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${x(o)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},es=i.memo(({toast:e,position:t,style:r,children:n})=>{let o=e.height?ei(e.position||t||"top-center",e.visible):{opacity:0},a=i.createElement(et,{toast:e}),s=i.createElement(ea,{...e.ariaProps},R(e.message,e));return i.createElement(eo,{className:e.className,style:{...o,...r,...e.style}},"function"==typeof n?n({icon:a,message:s}):i.createElement(i.Fragment,null,a,s))});a=i.createElement,p.p=void 0,b=a,g=void 0,E=void 0;var eu=({id:e,className:t,style:r,onHeightUpdate:n,children:o})=>{let a=i.useCallback(t=>{if(t){let r=()=>{n(e,t.getBoundingClientRect().height)};r(),new MutationObserver(r).observe(t,{subtree:!0,childList:!0,characterData:!0})}},[e,n]);return i.createElement("div",{ref:a,className:t,style:r},o)},el=(e,t)=>{let r=e.includes("top"),n=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:M()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(r?1:-1)}px)`,...r?{top:0}:{bottom:0},...n}},ec=y`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,ed=({reverseOrder:e,position:t="top-center",toastOptions:r,gutter:n,children:o,containerStyle:a,containerClassName:s})=>{let{toasts:u,handlers:l}=j(r);return i.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...a},className:s,onMouseEnter:l.startPause,onMouseLeave:l.endPause},u.map(r=>{let a=r.position||t,s=el(a,l.calculateOffset(r,{reverseOrder:e,gutter:n,defaultPosition:t}));return i.createElement(eu,{id:r.id,key:r.id,onHeightUpdate:l.updateHeight,className:r.visible?ec:"",style:s},"custom"===r.type?R(r.message,r):o?o(r):i.createElement(es,{toast:r,position:a}))}))},ep=L}}]);