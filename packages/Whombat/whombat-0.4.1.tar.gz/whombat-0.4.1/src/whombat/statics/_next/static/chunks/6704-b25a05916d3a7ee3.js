(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6704],{24033:function(e,t,o){e.exports=o(15313)},88180:function(e,t,o){"use strict";o.d(t,{h:function(){return K}});var r,n,a,i,l=o(2265),s=o(31860),u=o(82769),c=o(12950),d=o(75606),p=o(32600),f=o(61858),b=o(90583),m=o(8076),v=o(46618),x=o(50926),g=o(53891),h=o(85390),y=o(11931),R=o(35863),O=o(60597),C=o(28871),I=o(65410),T=o(58227),E=o(25306),S=o(93850),w=o(10841),P=o(7566),k=o(13995),M=o(34644),z=o(57728),A=((r=A||{})[r.Open=0]="Open",r[r.Closed=1]="Closed",r),D=((n=D||{})[n.Single=0]="Single",n[n.Multi=1]="Multi",n),N=((a=N||{})[a.Pointer=0]="Pointer",a[a.Other=1]="Other",a),F=((i=F||{})[i.OpenCombobox=0]="OpenCombobox",i[i.CloseCombobox=1]="CloseCombobox",i[i.GoToOption=2]="GoToOption",i[i.RegisterOption=3]="RegisterOption",i[i.UnregisterOption=4]="UnregisterOption",i[i.RegisterLabel=5]="RegisterLabel",i);function $(e,t=e=>e){let o=null!==e.activeOptionIndex?e.options[e.activeOptionIndex]:null,r=(0,I.z2)(t(e.options.slice()),e=>e.dataRef.current.domRef.current),n=o?r.indexOf(o):null;return -1===n&&(n=null),{options:r,activeOptionIndex:n}}let L={1(e){var t;return null!=(t=e.dataRef.current)&&t.disabled||1===e.comboboxState?e:{...e,activeOptionIndex:null,comboboxState:1}},0(e){var t;if(null!=(t=e.dataRef.current)&&t.disabled||0===e.comboboxState)return e;let o=e.activeOptionIndex;if(e.dataRef.current){let{isSelected:t}=e.dataRef.current,r=e.options.findIndex(e=>t(e.dataRef.current.value));-1!==r&&(o=r)}return{...e,comboboxState:0,activeOptionIndex:o}},2(e,t){var o,r,n,a;if(null!=(o=e.dataRef.current)&&o.disabled||null!=(r=e.dataRef.current)&&r.optionsRef.current&&!(null!=(n=e.dataRef.current)&&n.optionsPropsRef.current.static)&&1===e.comboboxState)return e;let i=$(e);if(null===i.activeOptionIndex){let e=i.options.findIndex(e=>!e.dataRef.current.disabled);-1!==e&&(i.activeOptionIndex=e)}let l=(0,g.d)(t,{resolveItems:()=>i.options,resolveActiveIndex:()=>i.activeOptionIndex,resolveId:e=>e.id,resolveDisabled:e=>e.dataRef.current.disabled});return{...e,...i,activeOptionIndex:l,activationTrigger:null!=(a=t.trigger)?a:1}},3:(e,t)=>{var o,r;let n={id:t.id,dataRef:t.dataRef},a=$(e,e=>[...e,n]);null===e.activeOptionIndex&&null!=(o=e.dataRef.current)&&o.isSelected(t.dataRef.current.value)&&(a.activeOptionIndex=a.options.indexOf(n));let i={...e,...a,activationTrigger:1};return null!=(r=e.dataRef.current)&&r.__demoMode&&void 0===e.dataRef.current.value&&(i.activeOptionIndex=0),i},4:(e,t)=>{let o=$(e,e=>{let o=e.findIndex(e=>e.id===t.id);return -1!==o&&e.splice(o,1),e});return{...e,...o,activationTrigger:1}},5:(e,t)=>({...e,labelId:t.id})},_=(0,l.createContext)(null);function j(e){let t=(0,l.useContext)(_);if(null===t){let t=Error(`<${e} /> is missing a parent <Combobox /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(t,j),t}return t}_.displayName="ComboboxActionsContext";let V=(0,l.createContext)(null);function q(e){let t=(0,l.useContext)(V);if(null===t){let t=Error(`<${e} /> is missing a parent <Combobox /> component.`);throw Error.captureStackTrace&&Error.captureStackTrace(t,q),t}return t}function B(e,t){return(0,O.E)(t.type,L,e,t)}V.displayName="ComboboxDataContext";let H=l.Fragment,U=y.AN.RenderStrategy|y.AN.Static,Y=(0,y.yV)(function(e,t){let{value:o,defaultValue:r,onChange:n,form:a,name:i,by:s=(e,t)=>e===t,disabled:d=!1,__demoMode:f=!1,nullable:m=!1,multiple:v=!1,...x}=e,[h=v?[]:void 0,R]=(0,w.q)(o,n,r),[I,S]=(0,l.useReducer)(B,{dataRef:(0,l.createRef)(),comboboxState:f?0:1,options:[],activeOptionIndex:null,activationTrigger:1,labelId:null}),P=(0,l.useRef)(!1),k=(0,l.useRef)({static:!1,hold:!1}),M=(0,l.useRef)(null),z=(0,l.useRef)(null),A=(0,l.useRef)(null),D=(0,l.useRef)(null),N=(0,c.z)("string"==typeof s?(e,t)=>(null==e?void 0:e[s])===(null==t?void 0:t[s]):s),F=(0,l.useCallback)(e=>(0,O.E)($.mode,{1:()=>h.some(t=>N(t,e)),0:()=>N(h,e)}),[h]),$=(0,l.useMemo)(()=>({...I,optionsPropsRef:k,labelRef:M,inputRef:z,buttonRef:A,optionsRef:D,value:h,defaultValue:r,disabled:d,mode:v?1:0,get activeOptionIndex(){if(P.current&&null===I.activeOptionIndex&&I.options.length>0){let e=I.options.findIndex(e=>!e.dataRef.current.disabled);if(-1!==e)return e}return I.activeOptionIndex},compare:N,isSelected:F,nullable:m,__demoMode:f}),[h,r,d,v,m,f,I]),L=(0,l.useRef)(null!==$.activeOptionIndex?$.options[$.activeOptionIndex]:null);(0,l.useEffect)(()=>{let e=null!==$.activeOptionIndex?$.options[$.activeOptionIndex]:null;L.current!==e&&(L.current=e)}),(0,p.e)(()=>{I.dataRef.current=$},[$]),(0,b.O)([$.buttonRef,$.inputRef,$.optionsRef],()=>Q.closeCombobox(),0===$.comboboxState);let j=(0,l.useMemo)(()=>({open:0===$.comboboxState,disabled:d,activeIndex:$.activeOptionIndex,activeOption:null===$.activeOptionIndex?null:$.options[$.activeOptionIndex].dataRef.current.value,value:h}),[$,d,h]),q=(0,c.z)(e=>{let t=$.options.find(t=>t.id===e);t&&W(t.dataRef.current.value)}),U=(0,c.z)(()=>{if(null!==$.activeOptionIndex){let{dataRef:e,id:t}=$.options[$.activeOptionIndex];W(e.current.value),Q.goToOption(g.T.Specific,t)}}),Y=(0,c.z)(()=>{S({type:0}),P.current=!0}),G=(0,c.z)(()=>{S({type:1}),P.current=!1}),K=(0,c.z)((e,t,o)=>(P.current=!1,e===g.T.Specific?S({type:2,focus:g.T.Specific,id:t,trigger:o}):S({type:2,focus:e,trigger:o}))),Z=(0,c.z)((e,t)=>(S({type:3,id:e,dataRef:t}),()=>{var t;(null==(t=L.current)?void 0:t.id)===e&&(P.current=!0),S({type:4,id:e})})),J=(0,c.z)(e=>(S({type:5,id:e}),()=>S({type:5,id:null}))),W=(0,c.z)(e=>(0,O.E)($.mode,{0:()=>null==R?void 0:R(e),1(){let t=$.value.slice(),o=t.findIndex(t=>N(t,e));return -1===o?t.push(e):t.splice(o,1),null==R?void 0:R(t)}})),Q=(0,l.useMemo)(()=>({onChange:W,registerOption:Z,registerLabel:J,goToOption:K,closeCombobox:G,openCombobox:Y,selectActiveOption:U,selectOption:q}),[]),X=(0,l.useRef)(null),ee=(0,u.G)();return(0,l.useEffect)(()=>{X.current&&void 0!==r&&ee.addEventListener(X.current,"reset",()=>{null==R||R(r)})},[X,R]),l.createElement(_.Provider,{value:Q},l.createElement(V.Provider,{value:$},l.createElement(E.up,{value:(0,O.E)($.comboboxState,{0:E.ZM.Open,1:E.ZM.Closed})},null!=i&&null!=h&&(0,C.t)({[i]:h}).map(([e,t],o)=>l.createElement(T._,{features:T.A.Hidden,ref:0===o?e=>{var t;X.current=null!=(t=null==e?void 0:e.closest("form"))?t:null}:void 0,...(0,y.oA)({key:e,as:"input",type:"hidden",hidden:!0,readOnly:!0,form:a,name:e,value:t})})),(0,y.sY)({ourProps:null===t?{}:{ref:t},theirProps:x,slot:j,defaultTag:H,name:"Combobox"}))))}),G=(0,y.yV)(function(e,t){var o;let r=q("Combobox.Button"),n=j("Combobox.Button"),a=(0,v.T)(r.buttonRef,t),i=(0,d.M)(),{id:p=`headlessui-combobox-button-${i}`,...f}=e,b=(0,u.G)(),x=(0,c.z)(e=>{switch(e.key){case S.R.ArrowDown:return e.preventDefault(),e.stopPropagation(),1===r.comboboxState&&n.openCombobox(),b.nextFrame(()=>{var e;return null==(e=r.inputRef.current)?void 0:e.focus({preventScroll:!0})});case S.R.ArrowUp:return e.preventDefault(),e.stopPropagation(),1===r.comboboxState&&(n.openCombobox(),b.nextFrame(()=>{r.value||n.goToOption(g.T.Last)})),b.nextFrame(()=>{var e;return null==(e=r.inputRef.current)?void 0:e.focus({preventScroll:!0})});case S.R.Escape:return 0!==r.comboboxState?void 0:(e.preventDefault(),r.optionsRef.current&&!r.optionsPropsRef.current.static&&e.stopPropagation(),n.closeCombobox(),b.nextFrame(()=>{var e;return null==(e=r.inputRef.current)?void 0:e.focus({preventScroll:!0})}));default:return}}),h=(0,c.z)(e=>{if((0,R.P)(e.currentTarget))return e.preventDefault();0===r.comboboxState?n.closeCombobox():(e.preventDefault(),n.openCombobox()),b.nextFrame(()=>{var e;return null==(e=r.inputRef.current)?void 0:e.focus({preventScroll:!0})})}),O=(0,s.v)(()=>{if(r.labelId)return[r.labelId,p].join(" ")},[r.labelId,p]),C=(0,l.useMemo)(()=>({open:0===r.comboboxState,disabled:r.disabled,value:r.value}),[r]),I={ref:a,id:p,type:(0,m.f)(e,r.buttonRef),tabIndex:-1,"aria-haspopup":"listbox","aria-controls":null==(o=r.optionsRef.current)?void 0:o.id,"aria-expanded":0===r.comboboxState,"aria-labelledby":O,disabled:r.disabled,onClick:h,onKeyDown:x};return(0,y.sY)({ourProps:I,theirProps:f,slot:C,defaultTag:"button",name:"Combobox.Button"})}),K=Object.assign(Y,{Input:(0,y.yV)(function(e,t){var o,r,n,a,i;let p=(0,d.M)(),{id:f=`headlessui-combobox-input-${p}`,onChange:b,displayValue:m,type:x="text",...h}=e,R=q("Combobox.Input"),C=j("Combobox.Input"),I=(0,v.T)(R.inputRef,t),T=(0,z.i)(R.inputRef),E=(0,l.useRef)(!1),w=(0,u.G)(),k=(0,c.z)(()=>{C.onChange(null),R.optionsRef.current&&(R.optionsRef.current.scrollTop=0),C.goToOption(g.T.Nothing)}),M="function"==typeof m&&void 0!==R.value?null!=(i=m(R.value))?i:"":"string"==typeof R.value?R.value:"";(0,P.q)(([e,t],[o,r])=>{if(E.current)return;let n=R.inputRef.current;n&&((0===r&&1===t||e!==o)&&(n.value=e),requestAnimationFrame(()=>{if(E.current||!n||(null==T?void 0:T.activeElement)!==n)return;let{selectionStart:e,selectionEnd:t}=n;0===Math.abs((null!=t?t:0)-(null!=e?e:0))&&0===e&&n.setSelectionRange(n.value.length,n.value.length)}))},[M,R.comboboxState,T]),(0,P.q)(([e],[t])=>{if(0===e&&1===t){if(E.current)return;let e=R.inputRef.current;if(!e)return;let t=e.value,{selectionStart:o,selectionEnd:r,selectionDirection:n}=e;e.value="",e.value=t,null!==n?e.setSelectionRange(o,r,n):e.setSelectionRange(o,r)}},[R.comboboxState]);let A=(0,l.useRef)(!1),D=(0,c.z)(()=>{A.current=!0}),N=(0,c.z)(()=>{w.nextFrame(()=>{A.current=!1})}),F=(0,c.z)(e=>{switch(E.current=!0,e.key){case S.R.Enter:if(E.current=!1,0!==R.comboboxState||A.current)return;if(e.preventDefault(),e.stopPropagation(),null===R.activeOptionIndex){C.closeCombobox();return}C.selectActiveOption(),0===R.mode&&C.closeCombobox();break;case S.R.ArrowDown:return E.current=!1,e.preventDefault(),e.stopPropagation(),(0,O.E)(R.comboboxState,{0:()=>{C.goToOption(g.T.Next)},1:()=>{C.openCombobox()}});case S.R.ArrowUp:return E.current=!1,e.preventDefault(),e.stopPropagation(),(0,O.E)(R.comboboxState,{0:()=>{C.goToOption(g.T.Previous)},1:()=>{C.openCombobox(),w.nextFrame(()=>{R.value||C.goToOption(g.T.Last)})}});case S.R.Home:if(e.shiftKey)break;return E.current=!1,e.preventDefault(),e.stopPropagation(),C.goToOption(g.T.First);case S.R.PageUp:return E.current=!1,e.preventDefault(),e.stopPropagation(),C.goToOption(g.T.First);case S.R.End:if(e.shiftKey)break;return E.current=!1,e.preventDefault(),e.stopPropagation(),C.goToOption(g.T.Last);case S.R.PageDown:return E.current=!1,e.preventDefault(),e.stopPropagation(),C.goToOption(g.T.Last);case S.R.Escape:return E.current=!1,0!==R.comboboxState?void 0:(e.preventDefault(),R.optionsRef.current&&!R.optionsPropsRef.current.static&&e.stopPropagation(),R.nullable&&0===R.mode&&null===R.value&&k(),C.closeCombobox());case S.R.Tab:if(E.current=!1,0!==R.comboboxState)return;0===R.mode&&C.selectActiveOption(),C.closeCombobox()}}),$=(0,c.z)(e=>{null==b||b(e),R.nullable&&0===R.mode&&""===e.target.value&&k(),C.openCombobox()}),L=(0,c.z)(()=>{E.current=!1}),_=(0,s.v)(()=>{if(R.labelId)return[R.labelId].join(" ")},[R.labelId]),V=(0,l.useMemo)(()=>({open:0===R.comboboxState,disabled:R.disabled}),[R]),B={ref:I,id:f,role:"combobox",type:x,"aria-controls":null==(o=R.optionsRef.current)?void 0:o.id,"aria-expanded":0===R.comboboxState,"aria-activedescendant":null===R.activeOptionIndex||null==(r=R.options[R.activeOptionIndex])?void 0:r.id,"aria-labelledby":_,"aria-autocomplete":"list",defaultValue:null!=(a=null!=(n=e.defaultValue)?n:void 0!==R.defaultValue?null==m?void 0:m(R.defaultValue):null)?a:R.defaultValue,disabled:R.disabled,onCompositionStart:D,onCompositionEnd:N,onKeyDown:F,onChange:$,onBlur:L};return(0,y.sY)({ourProps:B,theirProps:h,slot:V,defaultTag:"input",name:"Combobox.Input"})}),Button:G,Label:(0,y.yV)(function(e,t){let o=(0,d.M)(),{id:r=`headlessui-combobox-label-${o}`,...n}=e,a=q("Combobox.Label"),i=j("Combobox.Label"),s=(0,v.T)(a.labelRef,t);(0,p.e)(()=>i.registerLabel(r),[r]);let u=(0,c.z)(()=>{var e;return null==(e=a.inputRef.current)?void 0:e.focus({preventScroll:!0})}),f=(0,l.useMemo)(()=>({open:0===a.comboboxState,disabled:a.disabled}),[a]);return(0,y.sY)({ourProps:{ref:s,id:r,onClick:u},theirProps:n,slot:f,defaultTag:"label",name:"Combobox.Label"})}),Options:(0,y.yV)(function(e,t){let o=(0,d.M)(),{id:r=`headlessui-combobox-options-${o}`,hold:n=!1,...a}=e,i=q("Combobox.Options"),u=(0,v.T)(i.optionsRef,t),c=(0,E.oJ)(),f=null!==c?(c&E.ZM.Open)===E.ZM.Open:0===i.comboboxState;(0,p.e)(()=>{var t;i.optionsPropsRef.current.static=null!=(t=e.static)&&t},[i.optionsPropsRef,e.static]),(0,p.e)(()=>{i.optionsPropsRef.current.hold=n},[i.optionsPropsRef,n]),(0,x.B)({container:i.optionsRef.current,enabled:0===i.comboboxState,accept:e=>"option"===e.getAttribute("role")?NodeFilter.FILTER_REJECT:e.hasAttribute("role")?NodeFilter.FILTER_SKIP:NodeFilter.FILTER_ACCEPT,walk(e){e.setAttribute("role","none")}});let b=(0,s.v)(()=>{var e,t;return null!=(t=i.labelId)?t:null==(e=i.buttonRef.current)?void 0:e.id},[i.labelId,i.buttonRef.current]),m=(0,l.useMemo)(()=>({open:0===i.comboboxState}),[i]),g={"aria-labelledby":b,role:"listbox","aria-multiselectable":1===i.mode||void 0,id:r,ref:u};return(0,y.sY)({ourProps:g,theirProps:a,slot:m,defaultTag:"ul",features:U,visible:f,name:"Combobox.Options"})}),Option:(0,y.yV)(function(e,t){var o,r;let n=(0,d.M)(),{id:a=`headlessui-combobox-option-${n}`,disabled:i=!1,value:s,...u}=e,b=q("Combobox.Option"),m=j("Combobox.Option"),x=null!==b.activeOptionIndex&&b.options[b.activeOptionIndex].id===a,R=b.isSelected(s),O=(0,l.useRef)(null),C=(0,f.E)({disabled:i,value:s,domRef:O,textValue:null==(r=null==(o=O.current)?void 0:o.textContent)?void 0:r.toLowerCase()}),I=(0,v.T)(t,O),T=(0,c.z)(()=>m.selectOption(a));(0,p.e)(()=>m.registerOption(a,C),[C,a]);let E=(0,l.useRef)(!b.__demoMode);(0,p.e)(()=>{if(!b.__demoMode)return;let e=(0,h.k)();return e.requestAnimationFrame(()=>{E.current=!0}),e.dispose},[]),(0,p.e)(()=>{if(0!==b.comboboxState||!x||!E.current||0===b.activationTrigger)return;let e=(0,h.k)();return e.requestAnimationFrame(()=>{var e,t;null==(t=null==(e=O.current)?void 0:e.scrollIntoView)||t.call(e,{block:"nearest"})}),e.dispose},[O,x,b.comboboxState,b.activationTrigger,b.activeOptionIndex]);let S=(0,c.z)(e=>{if(i)return e.preventDefault();T(),0===b.mode&&m.closeCombobox(),(0,M.tq)()||requestAnimationFrame(()=>{var e;return null==(e=b.inputRef.current)?void 0:e.focus()})}),w=(0,c.z)(()=>{if(i)return m.goToOption(g.T.Nothing);m.goToOption(g.T.Specific,a)}),P=(0,k.g)(),z=(0,c.z)(e=>P.update(e)),A=(0,c.z)(e=>{P.wasMoved(e)&&(i||x||m.goToOption(g.T.Specific,a,0))}),D=(0,c.z)(e=>{P.wasMoved(e)&&(i||x&&(b.optionsPropsRef.current.hold||m.goToOption(g.T.Nothing)))}),N=(0,l.useMemo)(()=>({active:x,selected:R,disabled:i}),[x,R,i]);return(0,y.sY)({ourProps:{id:a,ref:I,role:"option",tabIndex:!0===i?void 0:-1,"aria-disabled":!0===i||void 0,"aria-selected":R,disabled:void 0,onClick:S,onFocus:w,onPointerEnter:z,onMouseEnter:z,onPointerMove:A,onMouseMove:A,onPointerLeave:D,onMouseLeave:D},theirProps:u,slot:N,defaultTag:"li",name:"Combobox.Option"})})})},50926:function(e,t,o){"use strict";o.d(t,{B:function(){return i}});var r=o(2265),n=o(32600),a=o(54851);function i({container:e,accept:t,walk:o,enabled:i=!0}){let l=(0,r.useRef)(t),s=(0,r.useRef)(o);(0,r.useEffect)(()=>{l.current=t,s.current=o},[t,o]),(0,n.e)(()=>{if(!e||!i)return;let t=(0,a.r)(e);if(!t)return;let o=l.current,r=s.current,n=Object.assign(e=>o(e),{acceptNode:o}),u=t.createTreeWalker(e,NodeFilter.SHOW_ELEMENT,n,!1);for(;u.nextNode();)r(u.currentNode)},[e,i,l,s])}},5925:function(e,t,o){"use strict";let r,n;o.d(t,{Ih:function(){return et},x7:function(){return ed},ZP:function(){return ep},GK:function(){return I},Am:function(){return L}});var a,i=o(2265);let l={data:""},s=e=>"object"==typeof window?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||l,u=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,c=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,p=(e,t)=>{let o="",r="",n="";for(let a in e){let i=e[a];"@"==a[0]?"i"==a[1]?o=a+" "+i+";":r+="f"==a[1]?p(i,a):a+"{"+p(i,"k"==a[1]?"":t)+"}":"object"==typeof i?r+=p(i,t?t.replace(/([^,])+/g,e=>a.replace(/(^:.*)|([^,])+/g,t=>/&/.test(t)?t.replace(/&/g,e):e?e+" "+t:t)):a):null!=i&&(a=/^--/.test(a)?a:a.replace(/[A-Z]/g,"-$&").toLowerCase(),n+=p.p?p.p(a,i):a+":"+i+";")}return o+(t&&n?t+"{"+n+"}":n)+r},f={},b=e=>{if("object"==typeof e){let t="";for(let o in e)t+=o+b(e[o]);return t}return e},m=(e,t,o,r,n)=>{var a;let i=b(e),l=f[i]||(f[i]=(e=>{let t=0,o=11;for(;t<e.length;)o=101*o+e.charCodeAt(t++)>>>0;return"go"+o})(i));if(!f[l]){let t=i!==e?e:(e=>{let t,o,r=[{}];for(;t=u.exec(e.replace(c,""));)t[4]?r.shift():t[3]?(o=t[3].replace(d," ").trim(),r.unshift(r[0][o]=r[0][o]||{})):r[0][t[1]]=t[2].replace(d," ").trim();return r[0]})(e);f[l]=p(n?{["@keyframes "+l]:t}:t,o?"":"."+l)}let s=o&&f.g?f.g:null;return o&&(f.g=f[l]),a=f[l],s?t.data=t.data.replace(s,a):-1===t.data.indexOf(a)&&(t.data=r?a+t.data:t.data+a),l},v=(e,t,o)=>e.reduce((e,r,n)=>{let a=t[n];if(a&&a.call){let e=a(o),t=e&&e.props&&e.props.className||/^go/.test(e)&&e;a=t?"."+t:e&&"object"==typeof e?e.props?"":p(e,""):!1===e?"":e}return e+r+(null==a?"":a)},"");function x(e){let t=this||{},o=e.call?e(t.p):e;return m(o.unshift?o.raw?v(o,[].slice.call(arguments,1),t.p):o.reduce((e,o)=>Object.assign(e,o&&o.call?o(t.p):o),{}):o,s(t.target),t.g,t.o,t.k)}x.bind({g:1});let g,h,y,R=x.bind({k:1});function O(e,t){let o=this||{};return function(){let r=arguments;function n(a,i){let l=Object.assign({},a),s=l.className||n.className;o.p=Object.assign({theme:h&&h()},l),o.o=/ *go\d+/.test(s),l.className=x.apply(o,r)+(s?" "+s:""),t&&(l.ref=i);let u=e;return e[0]&&(u=l.as||e,delete l.as),y&&u[0]&&y(l),g(u,l)}return t?t(n):n}}var C=e=>"function"==typeof e,I=(e,t)=>C(e)?e(t):e,T=(r=0,()=>(++r).toString()),E=()=>{if(void 0===n&&"u">typeof window){let e=matchMedia("(prefers-reduced-motion: reduce)");n=!e||e.matches}return n},S=new Map,w=e=>{if(S.has(e))return;let t=setTimeout(()=>{S.delete(e),A({type:4,toastId:e})},1e3);S.set(e,t)},P=e=>{let t=S.get(e);t&&clearTimeout(t)},k=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,20)};case 1:return t.toast.id&&P(t.toast.id),{...e,toasts:e.toasts.map(e=>e.id===t.toast.id?{...e,...t.toast}:e)};case 2:let{toast:o}=t;return e.toasts.find(e=>e.id===o.id)?k(e,{type:1,toast:o}):k(e,{type:0,toast:o});case 3:let{toastId:r}=t;return r?w(r):e.toasts.forEach(e=>{w(e.id)}),{...e,toasts:e.toasts.map(e=>e.id===r||void 0===r?{...e,visible:!1}:e)};case 4:return void 0===t.toastId?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(e=>e.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let n=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(e=>({...e,pauseDuration:e.pauseDuration+n}))}}},M=[],z={toasts:[],pausedAt:void 0},A=e=>{z=k(z,e),M.forEach(e=>{e(z)})},D={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},N=(e={})=>{let[t,o]=(0,i.useState)(z);(0,i.useEffect)(()=>(M.push(o),()=>{let e=M.indexOf(o);e>-1&&M.splice(e,1)}),[t]);let r=t.toasts.map(t=>{var o,r;return{...e,...e[t.type],...t,duration:t.duration||(null==(o=e[t.type])?void 0:o.duration)||(null==e?void 0:e.duration)||D[t.type],style:{...e.style,...null==(r=e[t.type])?void 0:r.style,...t.style}}});return{...t,toasts:r}},F=(e,t="blank",o)=>({createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...o,id:(null==o?void 0:o.id)||T()}),$=e=>(t,o)=>{let r=F(t,e,o);return A({type:2,toast:r}),r.id},L=(e,t)=>$("blank")(e,t);L.error=$("error"),L.success=$("success"),L.loading=$("loading"),L.custom=$("custom"),L.dismiss=e=>{A({type:3,toastId:e})},L.remove=e=>A({type:4,toastId:e}),L.promise=(e,t,o)=>{let r=L.loading(t.loading,{...o,...null==o?void 0:o.loading});return e.then(e=>(L.success(I(t.success,e),{id:r,...o,...null==o?void 0:o.success}),e)).catch(e=>{L.error(I(t.error,e),{id:r,...o,...null==o?void 0:o.error})}),e};var _=(e,t)=>{A({type:1,toast:{id:e,height:t}})},j=()=>{A({type:5,time:Date.now()})},V=e=>{let{toasts:t,pausedAt:o}=N(e);(0,i.useEffect)(()=>{if(o)return;let e=Date.now(),r=t.map(t=>{if(t.duration===1/0)return;let o=(t.duration||0)+t.pauseDuration-(e-t.createdAt);if(o<0){t.visible&&L.dismiss(t.id);return}return setTimeout(()=>L.dismiss(t.id),o)});return()=>{r.forEach(e=>e&&clearTimeout(e))}},[t,o]);let r=(0,i.useCallback)(()=>{o&&A({type:6,time:Date.now()})},[o]),n=(0,i.useCallback)((e,o)=>{let{reverseOrder:r=!1,gutter:n=8,defaultPosition:a}=o||{},i=t.filter(t=>(t.position||a)===(e.position||a)&&t.height),l=i.findIndex(t=>t.id===e.id),s=i.filter((e,t)=>t<l&&e.visible).length;return i.filter(e=>e.visible).slice(...r?[s+1]:[0,s]).reduce((e,t)=>e+(t.height||0)+n,0)},[t]);return{toasts:t,handlers:{updateHeight:_,startPause:j,endPause:r,calculateOffset:n}}},q=R`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,B=R`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,H=R`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,U=O("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${q} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${B} 0.15s ease-out forwards;
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
    animation: ${H} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,Y=R`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,G=O("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${Y} 1s linear infinite;
`,K=R`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,Z=R`
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
}`,J=O("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${K} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${Z} 0.2s ease-out forwards;
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
`,W=O("div")`
  position: absolute;
`,Q=O("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,X=R`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,ee=O("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${X} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,et=({toast:e})=>{let{icon:t,type:o,iconTheme:r}=e;return void 0!==t?"string"==typeof t?i.createElement(ee,null,t):t:"blank"===o?null:i.createElement(Q,null,i.createElement(G,{...r}),"loading"!==o&&i.createElement(W,null,"error"===o?i.createElement(U,{...r}):i.createElement(J,{...r})))},eo=e=>`
0% {transform: translate3d(0,${-200*e}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,er=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*e}%,-1px) scale(.6); opacity:0;}
`,en=O("div")`
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
`,ea=O("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,ei=(e,t)=>{let o=e.includes("top")?1:-1,[r,n]=E()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[eo(o),er(o)];return{animation:t?`${R(r)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${R(n)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},el=i.memo(({toast:e,position:t,style:o,children:r})=>{let n=e.height?ei(e.position||t||"top-center",e.visible):{opacity:0},a=i.createElement(et,{toast:e}),l=i.createElement(ea,{...e.ariaProps},I(e.message,e));return i.createElement(en,{className:e.className,style:{...n,...o,...e.style}},"function"==typeof r?r({icon:a,message:l}):i.createElement(i.Fragment,null,a,l))});a=i.createElement,p.p=void 0,g=a,h=void 0,y=void 0;var es=({id:e,className:t,style:o,onHeightUpdate:r,children:n})=>{let a=i.useCallback(t=>{if(t){let o=()=>{r(e,t.getBoundingClientRect().height)};o(),new MutationObserver(o).observe(t,{subtree:!0,childList:!0,characterData:!0})}},[e,r]);return i.createElement("div",{ref:a,className:t,style:o},n)},eu=(e,t)=>{let o=e.includes("top"),r=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:E()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(o?1:-1)}px)`,...o?{top:0}:{bottom:0},...r}},ec=x`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,ed=({reverseOrder:e,position:t="top-center",toastOptions:o,gutter:r,children:n,containerStyle:a,containerClassName:l})=>{let{toasts:s,handlers:u}=V(o);return i.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...a},className:l,onMouseEnter:u.startPause,onMouseLeave:u.endPause},s.map(o=>{let a=o.position||t,l=eu(a,u.calculateOffset(o,{reverseOrder:e,gutter:r,defaultPosition:t}));return i.createElement(es,{id:o.id,key:o.id,onHeightUpdate:u.updateHeight,className:o.visible?ec:"",style:l},"custom"===o.type?I(o.message,o):n?n(o):i.createElement(el,{toast:o,position:a}))}))},ep=L}}]);