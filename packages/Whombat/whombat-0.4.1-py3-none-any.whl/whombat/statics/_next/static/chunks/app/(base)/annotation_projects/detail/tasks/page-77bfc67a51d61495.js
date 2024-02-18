(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[7126],{10428:function(e,t,n){Promise.resolve().then(n.bind(n,55167))},83007:function(e,t,n){"use strict";let r=(0,n(2265).createContext)({name:"",description:"",tags:[],created_on:new Date,uuid:""});t.Z=r},55167:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return Z}});var r=n(57437),a=n(24033),s=n(2265),o=n(5925),i=n(68447),l=n(30143),c=n(50691),u=n(57760),d=n(59913),m=n(69761),f=n(2964),p=n(45987),h=n(90262),x=n(96883),g=n(17968),b=n(79105),y=n(14781);function v(e){let{annotationProject:t,onAddTasks:n}=e,a=(0,g.Z)({uuid:t.uuid,annotationProject:t,onAddAnnotationTasks:n}),[o,i]=(0,s.useState)(null),[l,c]=(0,s.useState)([]),[u,d]=(0,s.useState)([]);return(0,r.jsxs)("div",{className:"flex flex-col gap-8",children:[(0,r.jsxs)(f.H2,{children:[(0,r.jsx)(p.Fl,{className:"inline-block mr-2 w-5 h-5 align-middle"}),"Add Tasks"]}),(0,r.jsxs)("div",{className:"flex flex-row gap-8",children:[(0,r.jsxs)("div",{className:"flex flex-col gap-y-6 max-w-prose",children:[(0,r.jsx)("p",{className:"max-w-prose text-stone-500",children:"On this page, you can add tasks to your annotation project. Choose a dataset to pull recordings from, apply filters to narrow down your selection, and configure how audio clips are extracted from the chosen recordings."}),(0,r.jsx)(j,{selected:o,onSelect:i}),null!=o&&(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(w,{dataset:o,onSelection:c}),(0,r.jsx)(N,{onExtraction:d,selectedRecordings:l})]})]}),(0,r.jsx)("div",{className:"w-96",children:(0,r.jsx)("div",{className:"sticky top-8",children:(0,r.jsx)(k,{dataset:o,clips:u,recordings:l,onAdd:()=>a.addAnnotationTasks.mutate(u)})})})]})]})}function j(e){let{selected:t,onSelect:n}=e;return(0,r.jsxs)(l.Z,{children:[(0,r.jsxs)("div",{children:[(0,r.jsx)(f.H3,{className:"text-lg",children:"Select Dataset"}),(0,r.jsx)("p",{className:"text-stone-500",children:"Choose a dataset from which to source recordings."})]}),(0,r.jsx)(c.Z,{selected:t,onSelect:n})]})}function w(e){let{dataset:t,onSelection:n}=e,[a,o]=(0,s.useState)({subsample:!1,maxRecordings:5e3}),i=(0,s.useMemo)(()=>({dataset:t}),[t]),c=(0,b.Z)({pageSize:1e4,filter:i,fixed:["dataset"]});return(0,s.useEffect)(()=>{a.subsample?n([...(0,y.o)(c.items,a.maxRecordings)]):n([...c.items])},[t,a,c.items,n]),(0,r.jsxs)(l.Z,{children:[(0,r.jsxs)("div",{children:[(0,r.jsx)(f.H3,{className:"text-lg",children:"Select Recordings"}),(0,r.jsx)("p",{className:"text-stone-500",children:"Pick recordings to extract clips for your annotation project. Optionally, filter and choose a subset for clip extraction."})]}),(0,r.jsxs)("div",{className:"flex flex-col gap-4",children:[(0,r.jsx)(h.BZ,{name:"recording-filter",label:"Filter recordings",help:"Select a subset for clip extraction by applying filters.",children:(0,r.jsxs)("div",{className:"flex flex-row gap-2 items-center",children:[(0,r.jsx)("div",{className:"grow",children:(0,r.jsx)(u.Z,{showIfEmpty:!0,filter:c.filter,filterDef:m.Z})}),(0,r.jsx)(d.Z,{filter:c.filter,filterDef:m.Z,mode:"text",button:(0,r.jsxs)(r.Fragment,{children:["Add filters"," ",(0,r.jsx)(p.k1,{className:"inline-block w-4 h-4 stroke-2"})]})})]})}),(0,r.jsx)(h.BZ,{name:"subsample",label:"Subsample recordings",help:"Set a maximum for clip extraction. A random subset will be selected; all if not specified.",children:(0,r.jsxs)("div",{className:"inline-flex gap-3 items-center w-full",children:[(0,r.jsx)(x.Z,{isSelected:a.subsample,onChange:e=>o(t=>({...t,subsample:e}))}),(0,r.jsx)(h.II,{className:"grow",type:"number",placeholder:"Maximum number of recordings",value:a.subsample?a.maxRecordings:void 0,onChange:e=>o(t=>({...t,maxRecordings:e.target.valueAsNumber})),required:a.subsample,disabled:!a.subsample})]})})]})]})}function N(e){let{onExtraction:t,selectedRecordings:n}=e,[a,o]=(0,s.useState)({clipLength:10,subsample:!1,maxClipsPerRecording:10,clip:!0,overlap:0});return(0,s.useEffect)(()=>{t(function(e){let{recordings:t,config:n}=e,r=[],{clipLength:a,clip:s,subsample:o,overlap:i,maxClipsPerRecording:l}=n;for(let e of t){if(!s){r.push([e.uuid,{start_time:0,end_time:e.duration}]);continue}let t=[],n=Math.ceil(e.duration/(a-i));for(let r=0;r<n;r++){let n=r*(a-i),s=n+a;t.push([e.uuid,{start_time:n,end_time:s}])}if(!o){r.push(...t);continue}let c=(0,y.o)(t,l);r.push(...c)}return r}({recordings:n,config:a}))},[t,n,a]),(0,r.jsxs)(l.Z,{children:[(0,r.jsxs)("div",{children:[(0,r.jsx)(f.H3,{children:"Clip Extraction"}),(0,r.jsx)("p",{className:"text-stone-500",children:"Customize how to extract clips from the selected recordings."})]}),(0,r.jsx)(h.BZ,{name:"clip",label:"Should Clip",help:"Enable to extract smaller clips from the recordings; disable to use the entire recording as a clip.",children:(0,r.jsx)(x.Z,{isSelected:a.clip,onChange:e=>o(t=>({...t,clip:e}))})}),a.clip&&(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(h.BZ,{name:"clipLength",label:"Clip Length",help:"Specify the duration of each clip in seconds.",children:(0,r.jsx)(h.II,{type:"number",value:a.clipLength,onChange:e=>o(t=>({...t,clipLength:e.target.valueAsNumber})),required:!0})}),(0,r.jsx)(h.BZ,{name:"overlap",label:"Overlap",help:"Define the overlap duration between clips in seconds.",children:(0,r.jsx)(h.II,{type:"number",value:a.overlap,onChange:e=>o(t=>({...t,overlap:e.target.valueAsNumber})),required:!0})}),(0,r.jsx)(h.BZ,{name:"subsample",label:"Subsample clips",help:"Set a maximum number of clips to extract from each recording. A random subset will be selected. Leave empty to use all clips.",children:(0,r.jsxs)("div",{className:"inline-flex gap-3 items-center w-full",children:[(0,r.jsx)(x.Z,{isSelected:a.subsample,onChange:e=>o(t=>({...t,subsample:e}))}),(0,r.jsx)(h.II,{className:"grow",type:"number",placeholder:"Maximum clips per recording",value:a.subsample?a.maxClipsPerRecording:void 0,onChange:e=>o(t=>({...t,maxClipsPerRecording:e.target.valueAsNumber})),required:a.subsample,disabled:!a.subsample})]})})]})]})}function k(e){let{clips:t,dataset:n,recordings:a,onAdd:s}=e;return(0,r.jsxs)(l.Z,{children:[(0,r.jsx)(f.H3,{children:"Summary"}),null==n?(0,r.jsx)("p",{className:"text-stone-500",children:"Select a dataset to continue."}):(0,r.jsxs)(r.Fragment,{children:[(0,r.jsxs)("ul",{className:"list-disc list-inside",children:[(0,r.jsxs)("li",{children:["Selected dataset:"," ",(0,r.jsx)("span",{className:"text-emerald-500",children:n.name})]}),(0,r.jsxs)("li",{children:["Selected recordings:"," ",(0,r.jsx)("span",{className:"text-emerald-500",children:a.length})]}),(0,r.jsxs)("li",{children:["Tasks to add:"," ",(0,r.jsx)("span",{className:"font-bold text-emerald-500",children:t.length})]})]}),(0,r.jsx)("p",{className:"text-stone-500",children:"Once satisfied with your selections, click the button below to add the chosen clips to the annotation project."}),(0,r.jsx)(i.Z,{onClick:s,children:"Add Clips"})]})]})}var E=n(98771),C=n(83007);function Z(){let e=(0,s.useContext)(C.Z),t=(0,a.useRouter)(),n=(0,s.useCallback)(()=>{o.ZP.success("Tasks created"),t.push("/annotation_projects/detail/?annotation_project_uuid=".concat(e.uuid))},[e,t]);return null==e?(0,a.notFound)():(0,r.jsx)(E.Z,{children:(0,r.jsx)(v,{annotationProject:e,onAddTasks:n})})}},2964:function(e,t,n){"use strict";n.d(t,{H1:function(){return o},H2:function(){return i},H3:function(){return l},H4:function(){return c}});var r=n(57437),a=n(54440),s=n.n(a);function o(e){let{children:t,className:n,...a}=e;return(0,r.jsx)("h1",{className:s()("text-2xl font-bold text-stone-800 dark:text-stone-300",n),...a,children:t})}function i(e){let{children:t,className:n,...a}=e;return(0,r.jsx)("h2",{className:s()("text-xl font-bold text-stone-800 dark:text-stone-300",n),...a,children:t})}function l(e){let{children:t,className:n,...a}=e;return(0,r.jsx)("h3",{className:s()("text-lg font-semibold leading-7 items-center text-stone-800 dark:text-stone-300",n),...a,children:t})}function c(e){let{children:t,className:n,...a}=e;return(0,r.jsx)("h4",{className:s()(n,"text-md font-semibold leading-6 text-stone-800 dark:text-stone-300"),...a,children:t})}},69761:function(e,t,n){"use strict";var r=n(57437),a=n(97486),s=n(30818),o=n(45987);let i=[{name:"Duration",field:"duration",selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.P9,{name:"duration",onChange:e=>t("duration",e)})},render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Duration",value:t,onRemove:n})},description:"Select recordings by duration. Duration is in seconds.",icon:(0,r.jsx)(o.wZ,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{name:"Sample Rate",field:"samplerate",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Sample Rate",value:t,onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.P9,{onChange:e=>t("samplerate",e)})},icon:(0,r.jsx)(o.Dd,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{name:"Channels",field:"channels",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Channels",value:t,onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.P9,{onChange:e=>t("channels",e)})},icon:(0,r.jsx)(o.QE,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{field:"time_expansion",name:"Time Expansion",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Time Expansion",value:t,onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.P9,{onChange:e=>t("time_expansion",e)})},icon:(0,r.jsx)(o.i5,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{field:"latitude",name:"Latitude",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Latitude",value:t,onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.f3,{name:"latitude",onChange:e=>t("latitude",e)})},icon:(0,r.jsx)(o.cX,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{field:"longitude",name:"Longitude",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.V,{field:"Longitude",value:t,onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.f3,{name:"longitude",onChange:e=>t("longitude",e)})},icon:(0,r.jsx)(o.nU,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{field:"tag",name:"Has Tag",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.Z,{field:"Tag",value:"".concat(t.key,": ").concat(t.value),onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.D3,{onChange:e=>t("tag",e)})},icon:(0,r.jsx)(o.lO,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})},{field:"has_issues",name:"Has Issues",render:e=>{let{value:t,clear:n}=e;return(0,r.jsx)(a.Z,{field:"Has Issues",value:t?"Yes":"No",onRemove:n})},selector:e=>{let{setFilter:t}=e;return(0,r.jsx)(s.vN,{onChange:e=>t("has_issues",e)})},icon:(0,r.jsx)(o.uN,{className:"h-5 w-5 inline-block text-stone-500 mr-1 align-middle"})}];t.Z=i},98771:function(e,t,n){"use strict";n.d(t,{Z:function(){return a}});var r=n(57437);function a(e){let{children:t}=e;return(0,r.jsx)("div",{className:"flex flex-col justify-center items-center px-16 py-8 w-full",children:t})}},17968:function(e,t,n){"use strict";n.d(t,{Z:function(){return i}});var r=n(23588),a=n(2265),s=n(81698),o=n(41095);function i(e){let{uuid:t,annotationProject:n,onUpdate:i,onDelete:l,onAddTag:c,onRemoveTag:u,onAddAnnotationTasks:d,onError:m,enabled:f=!0}=e,{query:p,useMutation:h,client:x}=(0,o.ZP)({uuid:t,initial:n,name:"annotation_project",enabled:f,getFn:s.Z.annotationProjects.get,onError:m}),g=h({mutationFn:s.Z.annotationProjects.update,onSuccess:i}),b=h({mutationFn:s.Z.annotationProjects.addTag,onSuccess:c}),y=h({mutationFn:s.Z.annotationProjects.removeTag,onSuccess:u}),v=h({mutationFn:s.Z.annotationProjects.delete,onSuccess:l}),{data:j}=p,w=(0,a.useCallback)(async e=>{if(null==j)return;let t=await s.Z.clips.createMany(e);return await s.Z.annotationTasks.createMany(j,t)},[j]),N=(0,r.D)({mutationFn:w,onSuccess:e=>{null!=e&&(null==d||d(e),x.invalidateQueries({queryKey:["annotation_project",t]}))}}),k=(0,a.useMemo)(()=>{if(null!=j)return s.Z.annotationProjects.getDownloadUrl(j)},[j]);return{...p,update:g,addTag:b,addAnnotationTasks:N,removeTag:y,delete:v,download:k}}},79105:function(e,t,n){"use strict";n.d(t,{Z:function(){return d}});var r=n(2265),a=n(38038),s=n(23588),o=n(81698),i=n(35532),l=n(57022);let c={},u=[];function d(){let{filter:e=c,fixed:t=u,pageSize:n=20,enabled:d=!0}=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},m=(0,a.NL)(),f=(0,i.Z)({defaults:e,fixed:t}),{items:p,total:h,pagination:x,query:g,queryKey:b}=(0,l.Z)({name:"dataset_recordings",queryFn:o.Z.recordings.getMany,pageSize:n,filter:f.filter,enabled:d}),y=(0,r.useCallback)((e,t)=>{let{index:n}=t;m.setQueryData(b,t=>({...t,items:t.items.map((t,r)=>r!==n?t:e)}))},[m,b]),v=(0,r.useCallback)((e,t)=>{let{index:n}=t;m.setQueryData(b,e=>({...e,items:e.items.filter((e,t)=>t!==n)}))},[m,b]),j=(0,s.D)({mutationFn:async e=>{let{recording:t,data:n}=e;return await o.Z.recordings.update(t,n)},onSuccess:y}),w=(0,s.D)({mutationFn:async e=>{let{recording:t,tag:n}=e;return await o.Z.recordings.addTag(t,n)},onSuccess:y}),N=(0,s.D)({mutationFn:async e=>{let{recording:t,tag:n}=e;return await o.Z.recordings.removeTag(t,n)},onSuccess:y}),k=(0,s.D)({mutationFn:async e=>{let{recording:t}=e;return await o.Z.recordings.delete(t)},onSuccess:v});return{...g,items:p,total:h,pagination:x,filter:f,queryKey:b,updateRecording:j,addTag:w,removeTag:N,deleteRecording:k}}},41095:function(e,t,n){"use strict";n.d(t,{ZP:function(){return i}});var r=n(23588),a=n(67663),s=n(38038),o=n(2265);function i(e){let{uuid:t,initial:n,name:i,enabled:l=!0,getFn:c,onError:u}=e,d=(0,s.NL)(),m=(0,o.useCallback)(async()=>{if(null==t)throw Error("No uuid provided for object of type ".concat(i));return await c(t)},[t,i,c]),f=(0,a.a)({queryKey:[i,t],queryFn:m,retry:(e,t)=>{var n;if(null==t)return e<3;let r=null==t?void 0:null===(n=t.response)||void 0===n?void 0:n.status;return null==r?e<3:(!(r>=400)||!(r<500))&&e<3},initialData:n,staleTime:3e5,enabled:l&&null!=t}),p=(0,o.useCallback)(e=>{d.setQueryData([i,t],e)},[d,t,i]),{error:h,isError:x}=f;return(0,o.useEffect)(()=>{x&&(null==u||u(h))},[h,x,u]),{query:f,client:d,setData:p,useQuery:e=>{let{queryFn:n,name:r,enabled:s=!1}=e;return function(e){let{uuid:t,query:n,queryFn:r,name:s,secondaryName:i,enabled:l=!1}=e,{status:c,data:u}=n,d=(0,o.useCallback)(async()=>{if("pending"===c)throw Error("No data for object of type ".concat(s," (uuid=").concat(t,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===c)throw Error("Error while loading object of type ".concat(s," (uuid=").concat(t,"), cannot mutate"));return await r(u)},[c,u,r,s,t]);return(0,a.a)({queryFn:d,queryKey:[s,t,i],enabled:"pending"!==c&&"error"!==c&&l})}({uuid:t,query:f,queryFn:n,secondaryName:r,name:i,enabled:s})},useMutation:e=>{let{mutationFn:n,onSuccess:a,onError:s,withUpdate:l=!0}=e;return function(e){let{uuid:t,query:n,client:a,mutationFn:s,name:i,onSuccess:l,onError:c,withUpdate:u=!0}=e,{status:d,data:m}=n,f=(0,o.useCallback)(async e=>{if(null==t)throw Error("No uuid provided for object of type ".concat(i));if("pending"===d)throw Error("No data for object of type ".concat(i," (uuid=").concat(t,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===d)throw Error("Error while loading object of type ".concat(i," (uuid=").concat(t,"), cannot mutate"));return await s(m,e)},[d,m,s,i,t]);return(0,r.D)({mutationFn:f,onSuccess:e=>{u&&a.setQueryData([i,t],e),null==l||l(e)},onError:c})}({uuid:t,query:f,client:d,mutationFn:n,name:i,onSuccess:a,onError:s,withUpdate:l})},useDestruction:e=>{let{mutationFn:n,onSuccess:a,onError:s}=e;return function(e){let{uuid:t,query:n,client:a,mutationFn:s,name:i,onSuccess:l,onError:c}=e,{status:u,data:d}=n,m=(0,o.useCallback)(async()=>{if(null==t)throw Error("No uuid provided for object of type ".concat(i));if("pending"===u)throw Error("No data for object of type ".concat(i," (uuid=").concat(t,"). ")+"Either the query is not enabled or the query is still loading.");if("error"===u)throw Error("Error while loading object of type ".concat(i," (uuid=").concat(t,"), cannot mutate"));return await s(d)},[u,d,s,i,t]);return(0,r.D)({mutationFn:m,onSuccess:e=>{a.removeQueries({queryKey:[i,t]}),null==l||l(e)},onError:c})}({uuid:t,query:f,client:d,mutationFn:n,name:i,onSuccess:a,onError:s})}}}},14781:function(e,t,n){"use strict";function r(e){let t=e.slice(0);for(var n=t.length-1;n>0;n--){var r=Math.floor(Math.random()*(n+1)),a=t[n];t[n]=t[r],t[r]=a}return t}function a(e,t){for(var n,r,a=e.slice(0),s=e.length;s--;)n=a[r=Math.floor((s+1)*Math.random())],a[r]=a[s],a[s]=n;return a.slice(0,t)}n.d(t,{S:function(){return r},o:function(){return a}})},24033:function(e,t,n){e.exports=n(15313)},6890:function(e,t,n){"use strict";n.d(t,{O:function(){return s}});var r=n(2265),a=n(61858);function s(e,t,n,s){let o=(0,a.E)(n);(0,r.useEffect)(()=>{function n(e){o.current(e)}return(e=null!=e?e:window).addEventListener(t,n,s),()=>e.removeEventListener(t,n,s)},[e,t,s])}},59985:function(e,t,n){"use strict";n.d(t,{H:function(){return l},v:function(){return i}});var r=n(2265),a=n(58227),s=n(12950),o=n(57728);function i({defaultContainers:e=[],portals:t,mainTreeNodeRef:n}={}){var i;let l=(0,r.useRef)(null!=(i=null==n?void 0:n.current)?i:null),c=(0,o.i)(l),u=(0,s.z)(()=>{var n;let r=[];for(let t of e)null!==t&&(t instanceof HTMLElement?r.push(t):"current"in t&&t.current instanceof HTMLElement&&r.push(t.current));if(null!=t&&t.current)for(let e of t.current)r.push(e);for(let e of null!=(n=null==c?void 0:c.querySelectorAll("html > *, body > *"))?n:[])e!==document.body&&e!==document.head&&e instanceof HTMLElement&&"headlessui-portal-root"!==e.id&&(e.contains(l.current)||r.some(t=>e.contains(t))||r.push(e));return r});return{resolveContainers:u,contains:(0,s.z)(e=>u().some(t=>t.contains(e))),mainTreeNodeRef:l,MainTreeNode:(0,r.useMemo)(()=>function(){return null!=n?null:r.createElement(a._,{features:a.A.Hidden,ref:l})},[l,n])}}function l(){let e=(0,r.useRef)(null);return{mainTreeNodeRef:e,MainTreeNode:(0,r.useMemo)(()=>function(){return r.createElement(a._,{features:a.A.Hidden,ref:e})},[e])}}},49376:function(e,t,n){"use strict";n.d(t,{N:function(){return o},l:function(){return i}});var r,a=n(2265),s=n(27976),o=((r=o||{})[r.Forwards=0]="Forwards",r[r.Backwards=1]="Backwards",r);function i(){let e=(0,a.useRef)(0);return(0,s.s)("keydown",t=>{"Tab"===t.key&&(e.current=t.shiftKey?1:0)},!0),e}},5925:function(e,t,n){"use strict";let r,a;n.d(t,{Ih:function(){return et},x7:function(){return ed},ZP:function(){return em},GK:function(){return k},Am:function(){return L}});var s,o=n(2265);let i={data:""},l=e=>"object"==typeof window?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||i,c=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,u=/\/\*[^]*?\*\/|  +/g,d=/\n+/g,m=(e,t)=>{let n="",r="",a="";for(let s in e){let o=e[s];"@"==s[0]?"i"==s[1]?n=s+" "+o+";":r+="f"==s[1]?m(o,s):s+"{"+m(o,"k"==s[1]?"":t)+"}":"object"==typeof o?r+=m(o,t?t.replace(/([^,])+/g,e=>s.replace(/(^:.*)|([^,])+/g,t=>/&/.test(t)?t.replace(/&/g,e):e?e+" "+t:t)):s):null!=o&&(s=/^--/.test(s)?s:s.replace(/[A-Z]/g,"-$&").toLowerCase(),a+=m.p?m.p(s,o):s+":"+o+";")}return n+(t&&a?t+"{"+a+"}":a)+r},f={},p=e=>{if("object"==typeof e){let t="";for(let n in e)t+=n+p(e[n]);return t}return e},h=(e,t,n,r,a)=>{var s;let o=p(e),i=f[o]||(f[o]=(e=>{let t=0,n=11;for(;t<e.length;)n=101*n+e.charCodeAt(t++)>>>0;return"go"+n})(o));if(!f[i]){let t=o!==e?e:(e=>{let t,n,r=[{}];for(;t=c.exec(e.replace(u,""));)t[4]?r.shift():t[3]?(n=t[3].replace(d," ").trim(),r.unshift(r[0][n]=r[0][n]||{})):r[0][t[1]]=t[2].replace(d," ").trim();return r[0]})(e);f[i]=m(a?{["@keyframes "+i]:t}:t,n?"":"."+i)}let l=n&&f.g?f.g:null;return n&&(f.g=f[i]),s=f[i],l?t.data=t.data.replace(l,s):-1===t.data.indexOf(s)&&(t.data=r?s+t.data:t.data+s),i},x=(e,t,n)=>e.reduce((e,r,a)=>{let s=t[a];if(s&&s.call){let e=s(n),t=e&&e.props&&e.props.className||/^go/.test(e)&&e;s=t?"."+t:e&&"object"==typeof e?e.props?"":m(e,""):!1===e?"":e}return e+r+(null==s?"":s)},"");function g(e){let t=this||{},n=e.call?e(t.p):e;return h(n.unshift?n.raw?x(n,[].slice.call(arguments,1),t.p):n.reduce((e,n)=>Object.assign(e,n&&n.call?n(t.p):n),{}):n,l(t.target),t.g,t.o,t.k)}g.bind({g:1});let b,y,v,j=g.bind({k:1});function w(e,t){let n=this||{};return function(){let r=arguments;function a(s,o){let i=Object.assign({},s),l=i.className||a.className;n.p=Object.assign({theme:y&&y()},i),n.o=/ *go\d+/.test(l),i.className=g.apply(n,r)+(l?" "+l:""),t&&(i.ref=o);let c=e;return e[0]&&(c=i.as||e,delete i.as),v&&c[0]&&v(i),b(c,i)}return t?t(a):a}}var N=e=>"function"==typeof e,k=(e,t)=>N(e)?e(t):e,E=(r=0,()=>(++r).toString()),C=()=>{if(void 0===a&&"u">typeof window){let e=matchMedia("(prefers-reduced-motion: reduce)");a=!e||e.matches}return a},Z=new Map,S=e=>{if(Z.has(e))return;let t=setTimeout(()=>{Z.delete(e),R({type:4,toastId:e})},1e3);Z.set(e,t)},D=e=>{let t=Z.get(e);t&&clearTimeout(t)},P=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,20)};case 1:return t.toast.id&&D(t.toast.id),{...e,toasts:e.toasts.map(e=>e.id===t.toast.id?{...e,...t.toast}:e)};case 2:let{toast:n}=t;return e.toasts.find(e=>e.id===n.id)?P(e,{type:1,toast:n}):P(e,{type:0,toast:n});case 3:let{toastId:r}=t;return r?S(r):e.toasts.forEach(e=>{S(e.id)}),{...e,toasts:e.toasts.map(e=>e.id===r||void 0===r?{...e,visible:!1}:e)};case 4:return void 0===t.toastId?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(e=>e.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let a=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(e=>({...e,pauseDuration:e.pauseDuration+a}))}}},T=[],F={toasts:[],pausedAt:void 0},R=e=>{F=P(F,e),T.forEach(e=>{e(F)})},A={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},M=(e={})=>{let[t,n]=(0,o.useState)(F);(0,o.useEffect)(()=>(T.push(n),()=>{let e=T.indexOf(n);e>-1&&T.splice(e,1)}),[t]);let r=t.toasts.map(t=>{var n,r;return{...e,...e[t.type],...t,duration:t.duration||(null==(n=e[t.type])?void 0:n.duration)||(null==e?void 0:e.duration)||A[t.type],style:{...e.style,...null==(r=e[t.type])?void 0:r.style,...t.style}}});return{...t,toasts:r}},_=(e,t="blank",n)=>({createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...n,id:(null==n?void 0:n.id)||E()}),H=e=>(t,n)=>{let r=_(t,e,n);return R({type:2,toast:r}),r.id},L=(e,t)=>H("blank")(e,t);L.error=H("error"),L.success=H("success"),L.loading=H("loading"),L.custom=H("custom"),L.dismiss=e=>{R({type:3,toastId:e})},L.remove=e=>R({type:4,toastId:e}),L.promise=(e,t,n)=>{let r=L.loading(t.loading,{...n,...null==n?void 0:n.loading});return e.then(e=>(L.success(k(t.success,e),{id:r,...n,...null==n?void 0:n.success}),e)).catch(e=>{L.error(k(t.error,e),{id:r,...n,...null==n?void 0:n.error})}),e};var O=(e,t)=>{R({type:1,toast:{id:e,height:t}})},I=()=>{R({type:5,time:Date.now()})},$=e=>{let{toasts:t,pausedAt:n}=M(e);(0,o.useEffect)(()=>{if(n)return;let e=Date.now(),r=t.map(t=>{if(t.duration===1/0)return;let n=(t.duration||0)+t.pauseDuration-(e-t.createdAt);if(n<0){t.visible&&L.dismiss(t.id);return}return setTimeout(()=>L.dismiss(t.id),n)});return()=>{r.forEach(e=>e&&clearTimeout(e))}},[t,n]);let r=(0,o.useCallback)(()=>{n&&R({type:6,time:Date.now()})},[n]),a=(0,o.useCallback)((e,n)=>{let{reverseOrder:r=!1,gutter:a=8,defaultPosition:s}=n||{},o=t.filter(t=>(t.position||s)===(e.position||s)&&t.height),i=o.findIndex(t=>t.id===e.id),l=o.filter((e,t)=>t<i&&e.visible).length;return o.filter(e=>e.visible).slice(...r?[l+1]:[0,l]).reduce((e,t)=>e+(t.height||0)+a,0)},[t]);return{toasts:t,handlers:{updateHeight:O,startPause:I,endPause:r,calculateOffset:a}}},q=j`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,z=j`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,B=j`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,Q=w("div")`
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
    animation: ${z} 0.15s ease-out forwards;
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
    animation: ${B} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,K=j`
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
  animation: ${K} 1s linear infinite;
`,U=j`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,Y=j`
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

  animation: ${U} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${Y} 0.2s ease-out forwards;
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
`,X=w("div")`
  position: absolute;
`,J=w("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,W=j`
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
  animation: ${W} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,et=({toast:e})=>{let{icon:t,type:n,iconTheme:r}=e;return void 0!==t?"string"==typeof t?o.createElement(ee,null,t):t:"blank"===n?null:o.createElement(J,null,o.createElement(V,{...r}),"loading"!==n&&o.createElement(X,null,"error"===n?o.createElement(Q,{...r}):o.createElement(G,{...r})))},en=e=>`
0% {transform: translate3d(0,${-200*e}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,er=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${-150*e}%,-1px) scale(.6); opacity:0;}
`,ea=w("div")`
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
`,es=w("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,eo=(e,t)=>{let n=e.includes("top")?1:-1,[r,a]=C()?["0%{opacity:0;} 100%{opacity:1;}","0%{opacity:1;} 100%{opacity:0;}"]:[en(n),er(n)];return{animation:t?`${j(r)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${j(a)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},ei=o.memo(({toast:e,position:t,style:n,children:r})=>{let a=e.height?eo(e.position||t||"top-center",e.visible):{opacity:0},s=o.createElement(et,{toast:e}),i=o.createElement(es,{...e.ariaProps},k(e.message,e));return o.createElement(ea,{className:e.className,style:{...a,...n,...e.style}},"function"==typeof r?r({icon:s,message:i}):o.createElement(o.Fragment,null,s,i))});s=o.createElement,m.p=void 0,b=s,y=void 0,v=void 0;var el=({id:e,className:t,style:n,onHeightUpdate:r,children:a})=>{let s=o.useCallback(t=>{if(t){let n=()=>{r(e,t.getBoundingClientRect().height)};n(),new MutationObserver(n).observe(t,{subtree:!0,childList:!0,characterData:!0})}},[e,r]);return o.createElement("div",{ref:s,className:t,style:n},a)},ec=(e,t)=>{let n=e.includes("top"),r=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:C()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(n?1:-1)}px)`,...n?{top:0}:{bottom:0},...r}},eu=g`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,ed=({reverseOrder:e,position:t="top-center",toastOptions:n,gutter:r,children:a,containerStyle:s,containerClassName:i})=>{let{toasts:l,handlers:c}=$(n);return o.createElement("div",{style:{position:"fixed",zIndex:9999,top:16,left:16,right:16,bottom:16,pointerEvents:"none",...s},className:i,onMouseEnter:c.startPause,onMouseLeave:c.endPause},l.map(n=>{let s=n.position||t,i=ec(s,c.calculateOffset(n,{reverseOrder:e,gutter:r,defaultPosition:t}));return o.createElement(el,{id:n.id,key:n.id,onHeightUpdate:c.updateHeight,className:n.visible?eu:"",style:i},"custom"===n.type?k(n.message,n):a?a(n):o.createElement(ei,{toast:n,position:s}))}))},em=L}},function(e){e.O(0,[1749,9966,3475,8966,7663,828,721,3917,2403,5166,3302,1698,262,7548,457,2971,4938,1744],function(){return e(e.s=10428)}),_N_E=e.O()}]);