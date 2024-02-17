(window.webpackJsonpfeffery_utils_components=window.webpackJsonpfeffery_utils_components||[]).push([[23],{483:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var react__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(1),react__WEBPACK_IMPORTED_MODULE_0___default=__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__),_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(171),lodash__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(25),lodash__WEBPACK_IMPORTED_MODULE_2___default=__webpack_require__.n(lodash__WEBPACK_IMPORTED_MODULE_2__),ninja_keys__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(870),_components_FefferyStyle_react__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(88);function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function ownKeys(t,e){var n,i=Object.keys(t);return Object.getOwnPropertySymbols&&(n=Object.getOwnPropertySymbols(t),e&&(n=n.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),i.push.apply(i,n)),i}function _objectSpread(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?ownKeys(Object(n),!0).forEach(function(e){_defineProperty(t,e,n[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):ownKeys(Object(n)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))})}return t}function _defineProperty(e,t,n){(t=_toPropertyKey(t))in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n}function _toPropertyKey(e){e=_toPrimitive(e,"string");return"symbol"==_typeof(e)?e:String(e)}function _toPrimitive(e,t){if("object"!=_typeof(e)||!e)return e;var n=e[Symbol.toPrimitive];if(void 0===n)return("string"===t?String:Number)(e);n=n.call(e,t||"default");if("object"!=_typeof(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}var footerHtmlEn=react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div",{class:"modal-footer",slot:"footer"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{class:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"enter"),"to select"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"})),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"})),"to navigate"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"esc"),"to close"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"backspace"),"move to parent")),footerHtmlZh=react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div",{className:"modal-footer",slot:"footer"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"enter"),"选择"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"})),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"})),"上下切换"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"esc"),"关闭面板"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"backspace"),"回到上一级")),locale2footer=new Map([["en",footerHtmlEn],["zh",footerHtmlZh]]),locale2placeholder=new Map([["en","Type a command or search..."],["zh","输入指令或进行搜索..."]]),FefferyShortcutPanel=function FefferyShortcutPanel(props){var id=props.id,data=props.data,placeholder=props.placeholder,openHotkey=props.openHotkey,theme=props.theme,locale=props.locale,open=props.open,close=props.close,panelStyles=props.panelStyles,setProps=props.setProps,loading_state=props.loading_state,data=data.map(function(e){return Object(lodash__WEBPACK_IMPORTED_MODULE_2__.isString)(e.handler)||e.hasOwnProperty("children")?e:_objectSpread(_objectSpread({},e),{handler:function(){setProps({triggeredHotkey:{id:e.id,timestamp:Date.parse(new Date)}})}})}),ninjaKeys=Object(react__WEBPACK_IMPORTED_MODULE_0__.useRef)(null);return Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&ninjaKeys.current.addEventListener("change",function(e){setProps({searchValue:e.detail.search})})},[]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&(ninjaKeys.current.data=data.map(function(item){return Object(lodash__WEBPACK_IMPORTED_MODULE_2__.isString)(item.handler)?_objectSpread(_objectSpread({},item),{handler:eval(item.handler)}):item}))},[data]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&open&&(ninjaKeys.current.open(),setProps({open:!1}))},[open]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&close&&(ninjaKeys.current.close(),setProps({close:!1}))},[close]),panelStyles=_objectSpread(_objectSpread({},{width:"640px",overflowBackground:"rgba(255, 255, 255, 0.5)",textColor:"rgb(60, 65, 73)",fontSize:"16px",top:"20%",accentColor:"rgb(110, 94, 210)",secondaryBackgroundColor:"rgb(239, 241, 244)",secondaryTextColor:"rgb(107, 111, 118)",selectedBackground:"rgb(248, 249, 251)",actionsHeight:"300px",groupTextColor:"rgb(144, 149, 157)",zIndex:1}),panelStyles),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react__WEBPACK_IMPORTED_MODULE_0___default.a.Fragment,null,react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_components_FefferyStyle_react__WEBPACK_IMPORTED_MODULE_4__.a,{rawStyle:"\nninja-keys {\n    --ninja-width: ".concat(panelStyles.width,";\n    --ninja-overflow-background: ").concat(panelStyles.overflowBackground,";\n    --ninja-text-color: ").concat(panelStyles.textColor,";\n    --ninja-font-size: ").concat(panelStyles.fontSize,";\n    --ninja-top: ").concat(panelStyles.top,";\n    --ninja-accent-color: ").concat(panelStyles.accentColor,";\n    --ninja-secondary-background-color: ").concat(panelStyles.secondaryBackgroundColor,";\n    --ninja-secondary-text-color: ").concat(panelStyles.secondaryTextColor,";\n    --ninja-selected-background: ").concat(panelStyles.selectedBackground,";\n    --ninja-actions-height: ").concat(panelStyles.actionsHeight,";\n    --ninja-group-text-color: ").concat(panelStyles.groupTextColor,";\n    --ninja-z-index: ").concat(panelStyles.zIndex,";\n}\n")}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("ninja-keys",{id:id,class:theme,ref:ninjaKeys,placeholder:placeholder||locale2placeholder.get(locale),openHotkey:openHotkey,hotKeysJoinedView:!0,hideBreadcrumbs:!0,"data-dash-is-loading":loading_state&&loading_state.is_loading||void 0},locale2footer.get(locale)))};__webpack_exports__.default=FefferyShortcutPanel,FefferyShortcutPanel.defaultProps=_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__.b,FefferyShortcutPanel.propTypes=_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__.c},870:function(R,U,e){"use strict";const o=window,T=o.ShadowRoot&&(void 0===o.ShadyCSS||o.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,K=Symbol(),L=new WeakMap;class I{constructor(e,t,n){if(this._$cssResult$=!0,n!==K)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=t}get styleSheet(){let e=this.o;var t,n=this.t;return T&&void 0===e&&(t=void 0!==n&&1===n.length,void 0===(e=t?L.get(n):e))&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),t)&&L.set(n,e),e}toString(){return this.cssText}}const z=(i,...e)=>{e=1===i.length?i[0]:e.reduce((e,t,n)=>e+(()=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})()+i[n+1],i[0]);return new I(e,i,K)},N=T?e=>e:t=>{if(!(t instanceof CSSStyleSheet))return t;{let e="";for(const n of t.cssRules)e+=n.cssText;return t=e,new I("string"==typeof t?t:t+"",void 0,K)}};const W=window,V=W.trustedTypes,F=V?V.emptyScript:"",q=W.reactiveElementPolyfillSupport,G={toAttribute(e,t){switch(t){case Boolean:e=e?F:null;break;case Object:case Array:e=null==e?e:JSON.stringify(e)}return e},fromAttribute(e,t){let n=e;switch(t){case Boolean:n=null!==e;break;case Number:n=null===e?null:Number(e);break;case Object:case Array:try{n=JSON.parse(e)}catch(e){n=null}}return n}},J=(e,t)=>t!==e&&(t==t||e==e),Z={attribute:!0,type:String,converter:G,reflect:!1,hasChanged:J};class t extends HTMLElement{constructor(){super(),this._$Ei=new Map,this.isUpdatePending=!1,this.hasUpdated=!1,this._$El=null,this._$Eu()}static addInitializer(e){var t;this.finalize(),(null!=(t=this.h)?t:this.h=[]).push(e)}static get observedAttributes(){this.finalize();const n=[];return this.elementProperties.forEach((e,t)=>{e=this._$Ep(t,e);void 0!==e&&(this._$Ev.set(e,t),n.push(e))}),n}static createProperty(e,t=Z){var n;t.state&&(t.attribute=!1),this.finalize(),this.elementProperties.set(e,t),t.noAccessor||this.prototype.hasOwnProperty(e)||(n="symbol"==typeof e?Symbol():"__"+e,void 0!==(n=this.getPropertyDescriptor(e,n,t))&&Object.defineProperty(this.prototype,e,n))}static getPropertyDescriptor(n,i,o){return{get(){return this[i]},set(e){var t=this[n];this[i]=e,this.requestUpdate(n,t,o)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)||Z}static finalize(){if(this.hasOwnProperty("finalized"))return!1;this.finalized=!0;const e=Object.getPrototypeOf(this);if(e.finalize(),void 0!==e.h&&(this.h=[...e.h]),this.elementProperties=new Map(e.elementProperties),this._$Ev=new Map,this.hasOwnProperty("properties")){const e=this.properties,t=[...Object.getOwnPropertyNames(e),...Object.getOwnPropertySymbols(e)];for(const n of t)this.createProperty(n,e[n])}return this.elementStyles=this.finalizeStyles(this.styles),!0}static finalizeStyles(e){var t=[];if(Array.isArray(e)){var n=new Set(e.flat(1/0).reverse());for(const e of n)t.unshift(N(e))}else void 0!==e&&t.push(N(e));return t}static _$Ep(e,t){t=t.attribute;return!1===t?void 0:"string"==typeof t?t:"string"==typeof e?e.toLowerCase():void 0}_$Eu(){var e;this._$E_=new Promise(e=>this.enableUpdating=e),this._$AL=new Map,this._$Eg(),this.requestUpdate(),null!=(e=this.constructor.h)&&e.forEach(e=>e(this))}addController(e){var t;(null!=(t=this._$ES)?t:this._$ES=[]).push(e),void 0!==this.renderRoot&&this.isConnected&&null!=(t=e.hostConnected)&&t.call(e)}removeController(e){var t;null!=(t=this._$ES)&&t.splice(this._$ES.indexOf(e)>>>0,1)}_$Eg(){this.constructor.elementProperties.forEach((e,t)=>{this.hasOwnProperty(t)&&(this._$Ei.set(t,this[t]),delete this[t])})}createRenderRoot(){var i,e,t=null!=(t=this.shadowRoot)?t:this.attachShadow(this.constructor.shadowRootOptions);return i=t,e=this.constructor.elementStyles,T?i.adoptedStyleSheets=e.map(e=>e instanceof CSSStyleSheet?e:e.styleSheet):e.forEach(e=>{var t=document.createElement("style"),n=o.litNonce;void 0!==n&&t.setAttribute("nonce",n),t.textContent=e.cssText,i.appendChild(t)}),t}connectedCallback(){var e;void 0===this.renderRoot&&(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostConnected)?void 0:t.call(e)})}enableUpdating(e){}disconnectedCallback(){var e;null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostDisconnected)?void 0:t.call(e)})}attributeChangedCallback(e,t,n){this._$AK(e,n)}_$EO(e,t,n=Z){var i,o=this.constructor._$Ep(e,n);void 0!==o&&!0===n.reflect&&(i=(void 0!==(null==(i=n.converter)?void 0:i.toAttribute)?n.converter:G).toAttribute(t,n.type),this._$El=e,null==i?this.removeAttribute(o):this.setAttribute(o,i),this._$El=null)}_$AK(e,t){var n=this.constructor,i=n._$Ev.get(e);if(void 0!==i&&this._$El!==i){const e=n.getPropertyOptions(i),o="function"==typeof e.converter?{fromAttribute:e.converter}:void 0!==(null==(n=e.converter)?void 0:n.fromAttribute)?e.converter:G;this._$El=i,this[i]=o.fromAttribute(t,e.type),this._$El=null}}requestUpdate(e,t,n){let i=!0;void 0!==e&&(((n=n||this.constructor.getPropertyOptions(e)).hasChanged||J)(this[e],t)?(this._$AL.has(e)||this._$AL.set(e,t),!0===n.reflect&&this._$El!==e&&(void 0===this._$EC&&(this._$EC=new Map),this._$EC.set(e,n))):i=!1),!this.isUpdatePending&&i&&(this._$E_=this._$Ej())}async _$Ej(){this.isUpdatePending=!0;try{await this._$E_}catch(e){Promise.reject(e)}var e=this.scheduleUpdate();return null!=e&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var t;if(this.isUpdatePending){this.hasUpdated,this._$Ei&&(this._$Ei.forEach((e,t)=>this[t]=e),this._$Ei=void 0);let e=!1;var n=this._$AL;try{(e=this.shouldUpdate(n))?(this.willUpdate(n),null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdate)?void 0:t.call(e)}),this.update(n)):this._$Ek()}catch(t){throw e=!1,this._$Ek(),t}e&&this._$AE(n)}}willUpdate(e){}_$AE(e){var t;null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdated)?void 0:t.call(e)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$Ek(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$E_}shouldUpdate(e){return!0}update(e){void 0!==this._$EC&&(this._$EC.forEach((e,t)=>this._$EO(t,this[t],e)),this._$EC=void 0),this._$Ek()}updated(e){}firstUpdated(e){}}t.finalized=!0,t.elementProperties=new Map,t.elementStyles=[],t.shadowRootOptions={mode:"open"},null!=q&&q({ReactiveElement:t}),(null!=(n=W.reactiveElementVersions)?n:W.reactiveElementVersions=[]).push("1.6.3");const Q=window,c=Q.trustedTypes,X=c?c.createPolicy("lit-html",{createHTML:e=>e}):void 0,p=`lit$${(Math.random()+"").slice(9)}$`,Y="?"+p,ee=`<${Y}>`,l=document,h=()=>l.createComment(""),d=e=>null===e||"object"!=typeof e&&"function"!=typeof e,te=Array.isArray,ne=e=>te(e)||"function"==typeof(null==e?void 0:e[Symbol.iterator]),_=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,ie=/-->/g,oe=/>/g,u=RegExp(">|[ \t\n\f\r](?:([^\\s\"'>=/]+)([ \t\n\f\r]*=[ \t\n\f\r]*(?:[^ \t\n\f\r\"'`<>=]|(\"|')|))|$)","g"),se=/'/g,re=/"/g,ae=/^(?:script|style|textarea|title)$/i,le=n=>(e,...t)=>({_$litType$:n,strings:e,values:t}),s=le(1),f=(le(2),Symbol.for("lit-noChange")),v=Symbol.for("lit-nothing"),ce=new WeakMap,y=l.createTreeWalker(l,129,null,!1);function he(e,t){if(Array.isArray(e)&&e.hasOwnProperty("raw"))return void 0!==X?X.createHTML(t):t;throw Error("invalid template strings array")}const de=(s,e)=>{const r=s.length-1,a=[];let l,c=2===e?"<svg>":"",h=_;for(let o=0;o<r;o++){const r=s[o];let e,t,n=-1,i=0;for(;i<r.length&&(h.lastIndex=i,null!==(t=h.exec(r)));)i=h.lastIndex,h===_?"!--"===t[1]?h=ie:void 0!==t[1]?h=oe:void 0!==t[2]?(ae.test(t[2])&&(l=RegExp("</"+t[2],"g")),h=u):void 0!==t[3]&&(h=u):h===u?">"===t[0]?(h=null!=l?l:_,n=-1):void 0===t[1]?n=-2:(n=h.lastIndex-t[2].length,e=t[1],h=void 0===t[3]?u:'"'===t[3]?re:se):h===re||h===se?h=u:h===ie||h===oe?h=_:(h=u,l=void 0);var d=h===u&&s[o+1].startsWith("/>")?" ":"";c+=h===_?r+ee:0<=n?(a.push(e),r.slice(0,n)+"$lit$"+r.slice(n)+p+d):r+p+(-2===n?(a.push(void 0),o):d)}return[he(s,c+(s[r]||"<?>")+(2===e?"</svg>":"")),a]};class pe{constructor({strings:t,_$litType$:n},e){var i;this.parts=[];let o=0,s=0;var r=t.length-1,a=this.parts,[t,l]=de(t,n);if(this.el=pe.createElement(t,e),y.currentNode=this.el.content,2===n){const t=this.el.content,n=t.firstChild;n.remove(),t.append(...n.childNodes)}for(;null!==(i=y.nextNode())&&a.length<r;){if(1===i.nodeType){if(i.hasAttributes()){const t=[];for(const n of i.getAttributeNames())if(n.endsWith("$lit$")||n.startsWith(p)){const e=l[s++];if(t.push(n),void 0!==e){const t=i.getAttribute(e.toLowerCase()+"$lit$").split(p),n=/([.?@])?(.*)/.exec(e);a.push({type:1,index:o,name:n[2],strings:t,ctor:"."===n[1]?ue:"?"===n[1]?ve:"@"===n[1]?ye:b})}else a.push({type:6,index:o})}for(const n of t)i.removeAttribute(n)}if(ae.test(i.tagName)){const t=i.textContent.split(p),n=t.length-1;if(0<n){i.textContent=c?c.emptyScript:"";for(let e=0;e<n;e++)i.append(t[e],h()),y.nextNode(),a.push({type:2,index:++o});i.append(t[n],h())}}}else if(8===i.nodeType)if(i.data===Y)a.push({type:2,index:o});else{let e=-1;for(;-1!==(e=i.data.indexOf(p,e+1));)a.push({type:7,index:o}),e+=p.length-1}o++}}static createElement(e,t){var n=l.createElement("template");return n.innerHTML=e,n}}function m(t,n,i=t,o){var s;if(n!==f){let e=void 0!==o?null==(r=i._$Co)?void 0:r[o]:i._$Cl;var r=d(n)?void 0:n._$litDirective$;(null==e?void 0:e.constructor)!==r&&(null!=(s=null==e?void 0:e._$AO)&&s.call(e,!1),void 0===r?e=void 0:(e=new r(t))._$AT(t,i,o),void 0!==o?(null!=(s=i._$Co)?s:i._$Co=[])[o]=e:i._$Cl=e),void 0!==e&&(n=m(t,e._$AS(t,n.values),e,o))}return n}class _e{constructor(e,t){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=t}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(t){var{el:{content:e},parts:n}=this._$AD,i=(null!=(i=null==t?void 0:t.creationScope)?i:l).importNode(e,!0);y.currentNode=i;let o=y.nextNode(),s=0,r=0,a=n[0];for(;void 0!==a;){if(s===a.index){let e;2===a.type?e=new g(o,o.nextSibling,this,t):1===a.type?e=new a.ctor(o,a.name,a.strings,this,t):6===a.type&&(e=new me(o,this,t)),this._$AV.push(e),a=n[++r]}s!==(null==a?void 0:a.index)&&(o=y.nextNode(),s++)}return y.currentNode=l,i}v(e){let t=0;for(const n of this._$AV)void 0!==n&&(void 0!==n.strings?(n._$AI(e,n,t),t+=n.strings.length-2):n._$AI(e[t])),t++}}class g{constructor(e,t,n,i){this.type=2,this._$AH=v,this._$AN=void 0,this._$AA=e,this._$AB=t,this._$AM=n,this.options=i,this._$Cp=null==(e=null==i?void 0:i.isConnected)||e}get _$AU(){var e;return null!=(e=null==(e=this._$AM)?void 0:e._$AU)?e:this._$Cp}get parentNode(){let e=this._$AA.parentNode;var t=this._$AM;return e=void 0!==t&&11===(null==e?void 0:e.nodeType)?t.parentNode:e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,t=this){e=m(this,e,t),d(e)?e===v||null==e||""===e?(this._$AH!==v&&this._$AR(),this._$AH=v):e!==this._$AH&&e!==f&&this._(e):void 0!==e._$litType$?this.g(e):void 0!==e.nodeType?this.$(e):ne(e)?this.T(e):this._(e)}k(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}$(e){this._$AH!==e&&(this._$AR(),this._$AH=this.k(e))}_(e){this._$AH!==v&&d(this._$AH)?this._$AA.nextSibling.data=e:this.$(l.createTextNode(e)),this._$AH=e}g(e){var t,{values:n,_$litType$:i}=e,i="number"==typeof i?this._$AC(e):(void 0===i.el&&(i.el=pe.createElement(he(i.h,i.h[0]),this.options)),i);if((null==(t=this._$AH)?void 0:t._$AD)===i)this._$AH.v(n);else{const e=new _e(i,this),t=e.u(this.options);e.v(n),this.$(t),this._$AH=e}}_$AC(e){let t=ce.get(e.strings);return void 0===t&&ce.set(e.strings,t=new pe(e)),t}T(e){te(this._$AH)||(this._$AH=[],this._$AR());var t=this._$AH;let n,i=0;for(const o of e)i===t.length?t.push(n=new g(this.k(h()),this.k(h()),this,this.options)):n=t[i],n._$AI(o),i++;i<t.length&&(this._$AR(n&&n._$AB.nextSibling,i),t.length=i)}_$AR(e=this._$AA.nextSibling,t){var n;for(null!=(n=this._$AP)&&n.call(this,!1,!0,t);e&&e!==this._$AB;){const t=e.nextSibling;e.remove(),e=t}}setConnected(e){var t;void 0===this._$AM&&(this._$Cp=e,null!=(t=this._$AP))&&t.call(this,e)}}class b{constructor(e,t,n,i,o){this.type=1,this._$AH=v,this._$AN=void 0,this.element=e,this.name=t,this._$AM=i,this.options=o,2<n.length||""!==n[0]||""!==n[1]?(this._$AH=Array(n.length-1).fill(new String),this.strings=n):this._$AH=v}get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}_$AI(n,i=this,o,s){var r=this.strings;let a=!1;if(void 0===r)n=m(this,n,i,0),(a=!d(n)||n!==this._$AH&&n!==f)&&(this._$AH=n);else{const s=n;let e,t;for(n=r[0],e=0;e<r.length-1;e++)(t=m(this,s[o+e],i,e))===f&&(t=this._$AH[e]),a=a||!d(t)||t!==this._$AH[e],t===v?n=v:n!==v&&(n+=(null!=t?t:"")+r[e+1]),this._$AH[e]=t}a&&!s&&this.j(n)}j(e){e===v?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,null!=e?e:"")}}class ue extends b{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===v?void 0:e}}const fe=c?c.emptyScript:"";class ve extends b{constructor(){super(...arguments),this.type=4}j(e){e&&e!==v?this.element.setAttribute(this.name,fe):this.element.removeAttribute(this.name)}}class ye extends b{constructor(e,t,n,i,o){super(e,t,n,i,o),this.type=5}_$AI(e,t=this){var n,i;(e=null!=(t=m(this,e,t,0))?t:v)!==f&&(t=this._$AH,n=e===v&&t!==v||e.capture!==t.capture||e.once!==t.once||e.passive!==t.passive,i=e!==v&&(t===v||n),n&&this.element.removeEventListener(this.name,this,t),i&&this.element.addEventListener(this.name,this,e),this._$AH=e)}handleEvent(e){var t;"function"==typeof this._$AH?this._$AH.call(null!=(t=null==(t=this.options)?void 0:t.host)?t:this.element,e):this._$AH.handleEvent(e)}}class me{constructor(e,t,n){this.element=e,this.type=6,this._$AN=void 0,this._$AM=t,this.options=n}get _$AU(){return this._$AM._$AU}_$AI(e){m(this,e)}}var n={O:"$lit$",P:p,A:Y,C:1,M:de,L:_e,R:ne,D:m,I:g,V:b,H:ve,N:ye,U:ue,F:me},i=Q.litHtmlPolyfillSupport;null!=i&&i(pe,g),(null!=(i=Q.litHtmlVersions)?i:Q.litHtmlVersions=[]).push("2.8.0");class r extends t{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var e,t=super.createRenderRoot();return null==(e=this.renderOptions).renderBefore&&(e.renderBefore=t.firstChild),t}update(e){var t=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=((e,t,n)=>{var i,o=null!=(o=null==n?void 0:n.renderBefore)?o:t;let s=o._$litPart$;if(void 0===s){const e=null!=(i=null==n?void 0:n.renderBefore)?i:null;o._$litPart$=s=new g(t.insertBefore(h(),e),e,void 0,null!=n?n:{})}return s._$AI(e),s})(t,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),null!=(e=this._$Do)&&e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),null!=(e=this._$Do)&&e.setConnected(!1)}render(){return f}}r.finalized=!0,r._$litElement$=!0,null!=(i=globalThis.litElementHydrateSupport)&&i.call(globalThis,{LitElement:r});var i=globalThis.litElementPolyfillSupport;null!=i&&i({LitElement:r}),(null!=(i=globalThis.litElementVersions)?i:globalThis.litElementVersions=[]).push("3.3.3");const ge=o=>e=>{var t,n,i;return"function"!=typeof e?(t=o,{kind:i,elements:n}=e,{kind:i,elements:n,finisher(e){customElements.define(t,e)}}):(i=e,customElements.define(o,i),i)};function a(o){return(e,t)=>{return void 0!==t?void e.constructor.createProperty(t,o):(n=o,"method"!==(i=e).kind||!i.descriptor||"value"in i.descriptor?{kind:"field",key:Symbol(),placement:"own",descriptor:{},originalKey:i.key,initializer(){"function"==typeof i.initializer&&(this[i.key]=i.initializer.call(this))},finisher(e){e.createProperty(i.key,n)}}:{...i,finisher(e){e.createProperty(i.key,n)}});var n,i}}function E(e){return a({...e,state:!0})}null!=(i=window.HTMLSlotElement)&&i.prototype.assignedElements;const be=2,$=t=>(...e)=>({_$litDirective$:t,values:e});class w{constructor(e){}get _$AU(){return this._$AM._$AU}_$AT(e,t,n){this._$Ct=e,this._$AM=t,this._$Ci=n}_$AS(e,t){return this.update(e,t)}update(e,t){return this.render(...t)}}const Ee=n["I"],$e=e=>void 0===e.strings,we=()=>document.createComment(""),k=(t,n,i)=>{var o,s=t._$AA.parentNode,r=void 0===n?t._$AB:n._$AA;if(void 0===i){const n=s.insertBefore(we(),r),o=s.insertBefore(we(),r);i=new Ee(n,o,t,t.options)}else{const n=i._$AB.nextSibling,a=i._$AM,e=a!==t;if(e){let e;null!=(o=i._$AQ)&&o.call(i,t),i._$AM=t,void 0!==i._$AP&&(e=t._$AU)!==a._$AU&&i._$AP(e)}if(n!==r||e){let e=i._$AA;for(;e!==n;){const n=e.nextSibling;s.insertBefore(e,r),e=n}}}return i},A=(e,t,n=e)=>(e._$AI(t,n),e),ke={},Ae=(e,t=ke)=>e._$AH=t,je=e=>{var t;null!=(t=e._$AP)&&t.call(e,!1,!0);let n=e._$AA;for(var i=e._$AB.nextSibling;n!==i;){const e=n.nextSibling;n.remove(),n=e}},xe=(t,n,i)=>{var o=new Map;for(let e=n;e<=i;e++)o.set(t[e],e);return o},Pe=$(class extends w{constructor(e){if(super(e),e.type!==be)throw Error("repeat() can only be used in text expressions")}ct(e,t,n){let i;void 0===n?n=t:void 0!==t&&(i=t);var o=[],s=[];let r=0;for(const t of e)o[r]=i?i(t,r):r,s[r]=n(t,r),r++;return{values:s,keys:o}}render(e,t,n){return this.ct(e,t,n).values}update(e,[t,n,i]){var o=e._$AH,{values:s,keys:r}=this.ct(t,n,i);if(!Array.isArray(o))return this.ut=r,s;var a=null!=(t=this.ut)?t:this.ut=[],l=[];let c,h,d=0,p=o.length-1,_=0,u=s.length-1;for(;d<=p&&_<=u;)if(null===o[d])d++;else if(null===o[p])p--;else if(a[d]===r[_])l[_]=A(o[d],s[_]),d++,_++;else if(a[p]===r[u])l[u]=A(o[p],s[u]),p--,u--;else if(a[d]===r[u])l[u]=A(o[d],s[u]),k(e,l[u+1],o[d]),d++,u--;else if(a[p]===r[_])l[_]=A(o[p],s[_]),k(e,o[d],o[p]),p--,_++;else if(void 0===c&&(c=xe(r,_,u),h=xe(a,d,p)),c.has(a[d]))if(c.has(a[p])){const t=h.get(r[_]),n=void 0!==t?o[t]:null;if(null===n){const t=k(e,o[d]);A(t,s[_]),l[_]=t}else l[_]=A(n,s[_]),k(e,o[d],n),o[t]=null;_++}else je(o[p]),p--;else je(o[d]),d++;for(;_<=u;){const t=k(e,l[u+1]);A(t,s[_]),l[_++]=t}for(;d<=p;){const e=o[d++];null!==e&&je(e)}return this.ut=r,Ae(e,l),f}}),Oe=$(class extends w{constructor(e){if(super(e),3!==e.type&&1!==e.type&&4!==e.type)throw Error("The `live` directive is not allowed on child or event bindings");if(!$e(e))throw Error("`live` bindings can only contain a single expression")}render(e){return e}update(e,[t]){if(t!==f&&t!==v){var n=e.element,i=e.name;if(3===e.type){if(t===n[i])return f}else if(4===e.type){if(!!t===n.hasAttribute(i))return f}else if(1===e.type&&n.getAttribute(i)===t+"")return f;Ae(e)}return t}}),j=(e,t)=>{var n,i,o=e._$AN;if(void 0===o)return!1;for(const e of o)null!=(i=(n=e)._$AO)&&i.call(n,t,!1),j(e,t);return!0},Me=e=>{let t,n;for(;void 0!==(t=e._$AM)&&((n=t._$AN).delete(e),e=t,0===(null==n?void 0:n.size)););},Ce=n=>{for(let t;t=n._$AM;n=t){let e=t._$AN;if(void 0===e)t._$AN=e=new Set;else if(e.has(n))break;e.add(n),i=t,0,i.type==be&&(null==i._$AP&&(i._$AP=De),null==i._$AQ)&&(i._$AQ=Se)}var i};function Se(e){void 0!==this._$AN?(Me(this),this._$AM=e,Ce(this)):this._$AM=e}function De(e,t=!1,n=0){var i=this._$AH,o=this._$AN;if(void 0!==o&&0!==o.size)if(t)if(Array.isArray(i))for(let e=n;e<i.length;e++)j(i[e],!1),Me(i[e]);else null!=i&&(j(i,!1),Me(i));else j(this,e)}class He extends w{constructor(){super(...arguments),this._$AN=void 0}_$AT(e,t,n){super._$AT(e,t,n),Ce(this),this.isConnected=e._$AU}_$AO(e,t=!0){var n;e!==this.isConnected&&((this.isConnected=e)?null!=(n=this.reconnected)&&n.call(this):null!=(n=this.disconnected)&&n.call(this)),t&&(j(this,e),Me(this))}setValue(e){var t;$e(this._$Ct)?this._$Ct._$AI(e,this):((t=[...this._$Ct._$AH])[this._$Ci]=e,this._$Ct._$AI(t,this,0))}disconnected(){}reconnected(){}}const Be=()=>new Re;class Re{}const Ue=new WeakMap,Te=$(class extends He{render(e){return v}update(e,[t]){var n=t!==this.G;return n&&void 0!==this.G&&this.ot(void 0),!n&&this.rt===this.lt||(this.G=t,this.dt=null==(n=e.options)?void 0:n.host,this.ot(this.lt=e.element)),v}ot(t){if("function"==typeof this.G){var n=null!=(n=this.dt)?n:globalThis;let e=Ue.get(n);void 0===e&&(e=new WeakMap,Ue.set(n,e)),void 0!==e.get(this.G)&&this.G.call(this.dt,void 0),e.set(this.G,t),void 0!==t&&this.G.call(this.dt,t)}else this.G.value=t}get rt(){var e;return"function"==typeof this.G?null==(e=Ue.get(null!=(e=this.dt)?e:globalThis))?void 0:e.get(this.G):null==(e=this.G)?void 0:e.value}disconnected(){this.rt===this.lt&&this.ot(void 0)}reconnected(){this.ot(this.lt)}}),Ke=$(class extends w{constructor(e){if(super(e),1!==e.type||"class"!==e.name||2<(null==(e=e.strings)?void 0:e.length))throw Error("`classMap()` can only be used in the `class` attribute and must be the only part in the attribute.")}render(t){return" "+Object.keys(t).filter(e=>t[e]).join(" ")+" "}update(e,[t]){var n,i;if(void 0===this.it){this.it=new Set,void 0!==e.strings&&(this.nt=new Set(e.strings.join(" ").split(/\s/).filter(e=>""!==e)));for(const e in t)!t[e]||null!=(n=this.nt)&&n.has(e)||this.it.add(e);return this.render(t)}const o=e.element.classList;this.it.forEach(e=>{e in t||(o.remove(e),this.it.delete(e))});for(const e in t){const n=!!t[e];n===this.it.has(e)||null!=(i=this.nt)&&i.has(e)||(n?(o.add(e),this.it.add(e)):(o.remove(e),this.it.delete(e)))}return f}});i="undefined"!=typeof navigator&&0<navigator.userAgent.toLowerCase().indexOf("firefox");function Le(e,t,n){e.addEventListener?e.addEventListener(t,n,!1):e.attachEvent&&e.attachEvent("on".concat(t),function(){n(window.event)})}function Ie(e,t){for(var n=t.slice(0,t.length-1),i=0;i<n.length;i++)n[i]=e[n[i].toLowerCase()];return n}function ze(e){for(var t=(e=(e="string"!=typeof e?"":e).replace(/\s/g,"")).split(","),n=t.lastIndexOf("");0<=n;)t[n-1]+=",",t.splice(n,1),n=t.lastIndexOf("");return t}for(var Ne={backspace:8,tab:9,clear:12,enter:13,return:13,esc:27,escape:27,space:32,left:37,up:38,right:39,down:40,del:46,delete:46,ins:45,insert:45,home:36,end:35,pageup:33,pagedown:34,capslock:20,num_0:96,num_1:97,num_2:98,num_3:99,num_4:100,num_5:101,num_6:102,num_7:103,num_8:104,num_9:105,num_multiply:106,num_add:107,num_enter:108,num_subtract:109,num_decimal:110,num_divide:111,"⇪":20,",":188,".":190,"/":191,"`":192,"-":i?173:189,"=":i?61:187,";":i?59:186,"'":222,"[":219,"]":221,"\\":220},x={"⇧":16,shift:16,"⌥":18,alt:18,option:18,"⌃":17,ctrl:17,control:17,"⌘":91,cmd:91,command:91},We={16:"shiftKey",18:"altKey",17:"ctrlKey",91:"metaKey",shiftKey:16,ctrlKey:17,altKey:18,metaKey:91},P={16:!1,18:!1,17:!1,91:!1},O={},Ve=1;Ve<20;Ve++)Ne["f".concat(Ve)]=111+Ve;var M=[],Fe="all",qe=[],Ge=function(e){return Ne[e.toLowerCase()]||x[e.toLowerCase()]||e.toUpperCase().charCodeAt(0)};function Je(e){Fe=e||"all"}function C(){return Fe||"all"}function Ze(e){var t=e.key,i=e.scope,o=e.method,r=void 0===(e=e.splitKey)?"+":e;ze(t).forEach(function(e){var s,e=e.split(r),t=e.length,n=e[t-1],n="*"===n?"*":Ge(n);O[n]&&(i=i||C(),s=1<t?Ie(x,e):[],O[n]=O[n].map(function(e){return o&&e.method!==o||e.scope!==i||!function(e){for(var t=e.length>=s.length?e:s,n=e.length>=s.length?s:e,i=!0,o=0;o<t.length;o++)-1===n.indexOf(t[o])&&(i=!1);return i}(e.mods)?e:{}}))})}function Qe(e,t,n){var i;if(t.scope===n||"all"===t.scope){for(var o in i=0<t.mods.length,P)Object.prototype.hasOwnProperty.call(P,o)&&(!P[o]&&-1<t.mods.indexOf(+o)||P[o]&&-1===t.mods.indexOf(+o))&&(i=!1);(0!==t.mods.length||P[16]||P[18]||P[17]||P[91])&&!i&&"*"!==t.shortcut||!1===t.method(e,t)&&(e.preventDefault?e.preventDefault():e.returnValue=!1,e.stopPropagation&&e.stopPropagation(),e.cancelBubble)&&(e.cancelBubble=!0)}}function Xe(n){var e=O["*"],t=n.keyCode||n.which||n.charCode;if(S.filter.call(this,n)){if(-1===M.indexOf(t=93!==t&&224!==t?t:91)&&229!==t&&M.push(t),["ctrlKey","altKey","shiftKey","metaKey"].forEach(function(e){var t=We[e];n[e]&&-1===M.indexOf(t)?M.push(t):!n[e]&&-1<M.indexOf(t)?M.splice(M.indexOf(t),1):"metaKey"!==e||!n[e]||3!==M.length||n.ctrlKey||n.shiftKey||n.altKey||(M=M.slice(M.indexOf(t)))}),t in P){for(var i in P[t]=!0,x)x[i]===t&&(S[i]=!0);if(!e)return}for(var o in P)Object.prototype.hasOwnProperty.call(P,o)&&(P[o]=n[We[o]]);n.getModifierState&&(!n.altKey||n.ctrlKey)&&n.getModifierState("AltGraph")&&(-1===M.indexOf(17)&&M.push(17),-1===M.indexOf(18)&&M.push(18),P[17]=!0,P[18]=!0);var s=C();if(e)for(var r=0;r<e.length;r++)e[r].scope===s&&("keydown"===n.type&&e[r].keydown||"keyup"===n.type&&e[r].keyup)&&Qe(n,e[r],s);if(t in O)for(var a=0;a<O[t].length;a++)if(("keydown"===n.type&&O[t][a].keydown||"keyup"===n.type&&O[t][a].keyup)&&O[t][a].key){for(var l=O[t][a],c=l.splitKey,h=l.key.split(c),d=[],p=0;p<h.length;p++)d.push(Ge(h[p]));d.sort().join("")===M.sort().join("")&&Qe(n,l,s)}}}function S(e,t,n){M=[];var i=ze(e),o=[],s="all",r=document,a=0,l=!1,c=!0,h="+";for(void 0===n&&"function"==typeof t&&(n=t),"[object Object]"===Object.prototype.toString.call(t)&&(t.scope&&(s=t.scope),t.element&&(r=t.element),t.keyup&&(l=t.keyup),void 0!==t.keydown&&(c=t.keydown),"string"==typeof t.splitKey)&&(h=t.splitKey),"string"==typeof t&&(s=t);a<i.length;a++)o=[],1<(e=i[a].split(h)).length&&(o=Ie(x,e)),(e="*"===(e=e[e.length-1])?"*":Ge(e))in O||(O[e]=[]),O[e].push({keyup:l,keydown:c,scope:s,mods:o,shortcut:i[a],method:n,key:i[a],splitKey:h});void 0===r||(t=r,-1<qe.indexOf(t))||!window||(qe.push(r),Le(r,"keydown",function(e){Xe(e)}),Le(window,"focus",function(){M=[]}),Le(r,"keyup",function(e){Xe(e);var t=e.keyCode||e.which||e.charCode,n=M.indexOf(t);if(0<=n&&M.splice(n,1),e.key&&"meta"===e.key.toLowerCase()&&M.splice(0,M.length),(t=93!==t&&224!==t?t:91)in P)for(var i in P[t]=!1,x)x[i]===t&&(S[i]=!1)}))}var Ye,et,tt={setScope:Je,getScope:C,deleteScope:function(e,t){var n,i,o;for(o in e=e||C(),O)if(Object.prototype.hasOwnProperty.call(O,o))for(n=O[o],i=0;i<n.length;)n[i].scope===e?n.splice(i,1):i++;C()===e&&Je(t||"all")},getPressedKeyCodes:function(){return M.slice(0)},isPressed:function(e){return"string"==typeof e&&(e=Ge(e)),-1!==M.indexOf(e)},filter:function(e){var e=e.target||e.srcElement,t=e.tagName,n=!0;return n=!e.isContentEditable&&("INPUT"!==t&&"TEXTAREA"!==t&&"SELECT"!==t||e.readOnly)?n:!1},unbind:function(e){if(e){if(Array.isArray(e))e.forEach(function(e){e.key&&Ze(e)});else if("object"==typeof e)e.key&&Ze(e);else if("string"==typeof e){for(var t=arguments.length,n=new Array(1<t?t-1:0),i=1;i<t;i++)n[i-1]=arguments[i];var o=n[0],s=n[1];"function"==typeof o&&(s=o,o=""),Ze({key:e,scope:o,method:s,splitKey:"+"})}}else Object.keys(O).forEach(function(e){return delete O[e]})}};for(Ye in tt)Object.prototype.hasOwnProperty.call(tt,Ye)&&(S[Ye]=tt[Ye]);"undefined"!=typeof window&&(et=window.hotkeys,S.noConflict=function(e){return e&&window.hotkeys===S&&(window.hotkeys=et),S},window.hotkeys=S);function D(e,t,n,i){var o,s=arguments.length,r=s<3?t:null===i?i=Object.getOwnPropertyDescriptor(t,n):i;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)r=Reflect.decorate(e,t,n,i);else for(var a=e.length-1;0<=a;a--)(o=e[a])&&(r=(s<3?o(r):3<s?o(t,n,r):o(t,n))||r);return 3<s&&r&&Object.defineProperty(t,n,r),r}var H=S,n=class extends r{constructor(){super(...arguments),this.placeholder="",this.hideBreadcrumbs=!1,this.breadcrumbHome="Home",this.breadcrumbs=[],this._inputRef=Be()}render(){let e="";if(!this.hideBreadcrumbs){var t=[];for(const e of this.breadcrumbs)t.push(s`<button
            tabindex="-1"
            @click=${()=>this.selectParent(e)}
            class="breadcrumb"
          >
            ${e}
          </button>`);e=s`<div class="breadcrumb-list">
        <button
          tabindex="-1"
          @click=${()=>this.selectParent()}
          class="breadcrumb"
        >
          ${this.breadcrumbHome}
        </button>
        ${t}
      </div>`}return s`
      ${e}
      <div part="ninja-input-wrapper" class="search-wrapper">
        <input
          part="ninja-input"
          type="text"
          id="search"
          spellcheck="false"
          autocomplete="off"
          @input="${this._handleInput}"
          ${Te(this._inputRef)}
          placeholder="${this.placeholder}"
          class="search"
        />
      </div>
    `}setSearch(e){this._inputRef.value&&(this._inputRef.value.value=e)}focusSearch(){requestAnimationFrame(()=>this._inputRef.value.focus())}_handleInput(e){e=e.target;this.dispatchEvent(new CustomEvent("change",{detail:{search:e.value},bubbles:!1,composed:!1}))}selectParent(e){this.dispatchEvent(new CustomEvent("setParent",{detail:{parent:e},bubbles:!0,composed:!0}))}firstUpdated(){this.focusSearch()}_close(){this.dispatchEvent(new CustomEvent("close",{bubbles:!0,composed:!0}))}};n.styles=z`
    :host {
      flex: 1;
      position: relative;
    }
    .search {
      padding: 1.25em;
      flex-grow: 1;
      flex-shrink: 0;
      margin: 0px;
      border: none;
      appearance: none;
      font-size: 1.125em;
      background: transparent;
      caret-color: var(--ninja-accent-color);
      color: var(--ninja-text-color);
      outline: none;
      font-family: var(--ninja-font-family);
    }
    .search::placeholder {
      color: var(--ninja-placeholder-color);
    }
    .breadcrumb-list {
      padding: 1em 4em 0 1em;
      display: flex;
      flex-direction: row;
      align-items: stretch;
      justify-content: flex-start;
      flex: initial;
    }

    .breadcrumb {
      background: var(--ninja-secondary-background-color);
      text-align: center;
      line-height: 1.2em;
      border-radius: var(--ninja-key-border-radius);
      border: 0;
      cursor: pointer;
      padding: 0.1em 0.5em;
      color: var(--ninja-secondary-text-color);
      margin-right: 0.5em;
      outline: none;
      font-family: var(--ninja-font-family);
    }

    .search-wrapper {
      display: flex;
      border-bottom: var(--ninja-separate-border);
    }
  `,D([a()],n.prototype,"placeholder",void 0),D([a({type:Boolean})],n.prototype,"hideBreadcrumbs",void 0),D([a()],n.prototype,"breadcrumbHome",void 0),D([a({type:Array})],n.prototype,"breadcrumbs",void 0),D([ge("ninja-header")],n);class nt extends w{constructor(e){if(super(e),this.et=v,e.type!==be)throw Error(this.constructor.directiveName+"() can only be used in child bindings")}render(e){if(e===v||null==e)return this.ft=void 0,this.et=e;if(e===f)return e;if("string"!=typeof e)throw Error(this.constructor.directiveName+"() called with a non-string value");return e===this.et?this.ft:(e=[this.et=e],this.ft={_$litType$:this.constructor.resultType,strings:e.raw=e,values:[]})}}nt.directiveName="unsafeHTML",nt.resultType=1;const it=$(nt);function ot(e,t,n,i){var o,s=arguments.length,r=s<3?t:null===i?i=Object.getOwnPropertyDescriptor(t,n):i;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)r=Reflect.decorate(e,t,n,i);else for(var a=e.length-1;0<=a;a--)(o=e[a])&&(r=(s<3?o(r):3<s?o(t,n,r):o(t,n))||r);return 3<s&&r&&Object.defineProperty(t,n,r),r}i=e(2),n=z`:host{font-family:var(--mdc-icon-font, "Material Icons");font-weight:normal;font-style:normal;font-size:var(--mdc-icon-size, 24px);line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;-moz-osx-font-smoothing:grayscale;font-feature-settings:"liga"}`,e=class extends r{render(){return s`<span><slot></slot></span>`}},e.styles=[n],Object(i.c)([ge("mwc-icon")],e),n=class extends r{constructor(){super(),this.selected=!1,this.hotKeysJoinedView=!0,this.addEventListener("click",this.click)}ensureInView(){requestAnimationFrame(()=>this.scrollIntoView({block:"nearest"}))}click(){this.dispatchEvent(new CustomEvent("actionsSelected",{detail:this.action,bubbles:!0,composed:!0}))}updated(e){e.has("selected")&&this.selected&&this.ensureInView()}render(){let e,t;this.action.mdIcon?e=s`<mwc-icon part="ninja-icon" class="ninja-icon"
        >${this.action.mdIcon}</mwc-icon
      >`:this.action.icon&&(e=it(this.action.icon||"")),this.action.hotkey&&(t=this.hotKeysJoinedView?this.action.hotkey.split(",").map(e=>{e=e.split("+"),e=s`${function*(t){if(void 0!==t){let e=-1;for(const n of t)-1<e&&(yield"+"),e++,yield n}}(e.map(e=>s`<kbd>${e}</kbd>`))}`;return s`<div class="ninja-hotkey ninja-hotkeys">
            ${e}
          </div>`}):this.action.hotkey.split(",").map(e=>{e=e.split("+").map(e=>s`<kbd class="ninja-hotkey">${e}</kbd>`);return s`<kbd class="ninja-hotkeys">${e}</kbd>`}));var n={selected:this.selected,"ninja-action":!0};return s`
      <div
        class="ninja-action"
        part="ninja-action ${this.selected?"ninja-selected":""}"
        class=${Ke(n)}
      >
        ${e}
        <div class="ninja-title">${this.action.title}</div>
        ${t}
      </div>
    `}};n.styles=z`
    :host {
      display: flex;
      width: 100%;
    }
    .ninja-action {
      padding: 0.75em 1em;
      display: flex;
      border-left: 2px solid transparent;
      align-items: center;
      justify-content: start;
      outline: none;
      transition: color 0s ease 0s;
      width: 100%;
    }
    .ninja-action.selected {
      cursor: pointer;
      color: var(--ninja-selected-text-color);
      background-color: var(--ninja-selected-background);
      border-left: 2px solid var(--ninja-accent-color);
      outline: none;
    }
    .ninja-action.selected .ninja-icon {
      color: var(--ninja-selected-text-color);
    }
    .ninja-icon {
      font-size: var(--ninja-icon-size);
      max-width: var(--ninja-icon-size);
      max-height: var(--ninja-icon-size);
      margin-right: 1em;
      color: var(--ninja-icon-color);
      margin-right: 1em;
      position: relative;
    }

    .ninja-title {
      flex-shrink: 0.01;
      margin-right: 0.5em;
      flex-grow: 1;
      font-size: 0.8125em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .ninja-hotkeys {
      flex-shrink: 0;
      width: min-content;
      display: flex;
    }

    .ninja-hotkeys kbd {
      font-family: inherit;
    }
    .ninja-hotkey {
      background: var(--ninja-secondary-background-color);
      padding: 0.06em 0.25em;
      border-radius: var(--ninja-key-border-radius);
      text-transform: capitalize;
      color: var(--ninja-secondary-text-color);
      font-size: 0.75em;
      font-family: inherit;
    }

    .ninja-hotkey + .ninja-hotkey {
      margin-left: 0.5em;
    }
    .ninja-hotkeys + .ninja-hotkeys {
      margin-left: 1em;
    }
  `,ot([a({type:Object})],n.prototype,"action",void 0),ot([a({type:Boolean})],n.prototype,"selected",void 0),ot([a({type:Boolean})],n.prototype,"hotKeysJoinedView",void 0),ot([ge("ninja-action")],n);const st=s` <div class="modal-footer" slot="footer">
  <span class="help">
    <svg
      version="1.0"
      class="ninja-examplekey"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1280 1280"
    >
      <path
        d="M1013 376c0 73.4-.4 113.3-1.1 120.2a159.9 159.9 0 0 1-90.2 127.3c-20 9.6-36.7 14-59.2 15.5-7.1.5-121.9.9-255 1h-242l95.5-95.5 95.5-95.5-38.3-38.2-38.2-38.3-160 160c-88 88-160 160.4-160 161 0 .6 72 73 160 161l160 160 38.2-38.3 38.3-38.2-95.5-95.5-95.5-95.5h251.1c252.9 0 259.8-.1 281.4-3.6 72.1-11.8 136.9-54.1 178.5-116.4 8.6-12.9 22.6-40.5 28-55.4 4.4-12 10.7-36.1 13.1-50.6 1.6-9.6 1.8-21 2.1-132.8l.4-122.2H1013v110z"
      />
    </svg>

    to select
  </span>
  <span class="help">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey"
      viewBox="0 0 24 24"
    >
      <path d="M0 0h24v24H0V0z" fill="none" />
      <path
        d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"
      />
    </svg>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey"
      viewBox="0 0 24 24"
    >
      <path d="M0 0h24v24H0V0z" fill="none" />
      <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z" />
    </svg>
    to navigate
  </span>
  <span class="help">
    <span class="ninja-examplekey esc">esc</span>
    to close
  </span>
  <span class="help">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey backspace"
      viewBox="0 0 20 20"
      fill="currentColor"
    >
      <path
        fill-rule="evenodd"
        d="M6.707 4.879A3 3 0 018.828 4H15a3 3 0 013 3v6a3 3 0 01-3 3H8.828a3 3 0 01-2.12-.879l-4.415-4.414a1 1 0 010-1.414l4.414-4.414zm4 2.414a1 1 0 00-1.414 1.414L10.586 10l-1.293 1.293a1 1 0 101.414 1.414L12 11.414l1.293 1.293a1 1 0 001.414-1.414L13.414 10l1.293-1.293a1 1 0 00-1.414-1.414L12 8.586l-1.293-1.293z"
        clip-rule="evenodd"
      />
    </svg>
    move to parent
  </span>
</div>`,rt=z`
  :host {
    --ninja-width: 640px;
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(255, 255, 255, 0.5);
    --ninja-text-color: rgb(60, 65, 73);
    --ninja-font-size: 16px;
    --ninja-top: 20%;

    --ninja-key-border-radius: 0.25em;
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgb(239, 241, 244);
    --ninja-secondary-text-color: rgb(107, 111, 118);

    --ninja-selected-background: rgb(248, 249, 251);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-icon-size: 1.2em;
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-background: #fff;
    --ninja-modal-shadow: rgb(0 0 0 / 50%) 0px 16px 70px;

    --ninja-actions-height: 300px;
    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(242, 242, 242, 0.4);

    --ninja-placeholder-color: #8e8e8e;

    font-size: var(--ninja-font-size);

    --ninja-z-index: 1;
  }

  :host(.dark) {
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(0, 0, 0, 0.7);
    --ninja-text-color: #7d7d7d;

    --ninja-modal-background: rgba(17, 17, 17, 0.85);
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgba(51, 51, 51, 0.44);
    --ninja-secondary-text-color: #888;

    --ninja-selected-text-color: #eaeaea;
    --ninja-selected-background: rgba(51, 51, 51, 0.44);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-shadow: 0 16px 70px rgba(0, 0, 0, 0.2);

    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(30, 30, 30, 85%);
  }

  .modal {
    display: none;
    position: fixed;
    z-index: var(--ninja-z-index);
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background: var(--ninja-overflow-background);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-backdrop-filter: var(--ninja-backdrop-filter);
    backdrop-filter: var(--ninja-backdrop-filter);
    text-align: left;
    color: var(--ninja-text-color);
    font-family: var(--ninja-font-family);
  }
  .modal.visible {
    display: block;
  }

  .modal-content {
    position: relative;
    top: var(--ninja-top);
    margin: auto;
    padding: 0;
    display: flex;
    flex-direction: column;
    flex-shrink: 1;
    -webkit-box-flex: 1;
    flex-grow: 1;
    min-width: 0px;
    will-change: transform;
    background: var(--ninja-modal-background);
    border-radius: 0.5em;
    box-shadow: var(--ninja-modal-shadow);
    max-width: var(--ninja-width);
    overflow: hidden;
  }

  .bump {
    animation: zoom-in-zoom-out 0.2s ease;
  }

  @keyframes zoom-in-zoom-out {
    0% {
      transform: scale(0.99);
    }
    50% {
      transform: scale(1.01, 1.01);
    }
    100% {
      transform: scale(1, 1);
    }
  }

  .ninja-github {
    color: var(--ninja-keys-text-color);
    font-weight: normal;
    text-decoration: none;
  }

  .actions-list {
    max-height: var(--ninja-actions-height);
    overflow: auto;
    scroll-behavior: smooth;
    position: relative;
    margin: 0;
    padding: 0.5em 0;
    list-style: none;
    scroll-behavior: smooth;
  }

  .group-header {
    height: 1.375em;
    line-height: 1.375em;
    padding-left: 1.25em;
    padding-top: 0.5em;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    font-size: 0.75em;
    line-height: 1em;
    color: var(--ninja-group-text-color);
    margin: 1px 0;
  }

  .modal-footer {
    background: var(--ninja-footer-background);
    padding: 0.5em 1em;
    display: flex;
    /* font-size: 0.75em; */
    border-top: var(--ninja-separate-border);
    color: var(--ninja-secondary-text-color);
  }

  .modal-footer .help {
    display: flex;
    margin-right: 1em;
    align-items: center;
    font-size: 0.75em;
  }

  .ninja-examplekey {
    background: var(--ninja-secondary-background-color);
    padding: 0.06em 0.25em;
    border-radius: var(--ninja-key-border-radius);
    color: var(--ninja-secondary-text-color);
    width: 1em;
    height: 1em;
    margin-right: 0.5em;
    font-size: 1.25em;
    fill: currentColor;
  }
  .ninja-examplekey.esc {
    width: auto;
    height: auto;
    font-size: 1.1em;
  }
  .ninja-examplekey.backspace {
    opacity: 0.7;
  }
`;function B(e,t,n,i){var o,s=arguments.length,r=s<3?t:null===i?i=Object.getOwnPropertyDescriptor(t,n):i;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)r=Reflect.decorate(e,t,n,i);else for(var a=e.length-1;0<=a;a--)(o=e[a])&&(r=(s<3?o(r):3<s?o(t,n,r):o(t,n))||r);return 3<s&&r&&Object.defineProperty(t,n,r),r}i=class extends r{constructor(){super(...arguments),this.placeholder="Type a command or search...",this.disableHotkeys=!1,this.hideBreadcrumbs=!1,this.openHotkey="cmd+k,ctrl+k",this.navigationUpHotkey="up,shift+tab",this.navigationDownHotkey="down,tab",this.closeHotkey="esc",this.goBackHotkey="backspace",this.selectHotkey="enter",this.hotKeysJoinedView=!1,this.noAutoLoadMdIcons=!1,this.data=[],this.visible=!1,this._bump=!0,this._actionMatches=[],this._search="",this._flatData=[],this._headerRef=Be()}open(e={}){this._bump=!0,this.visible=!0,this._headerRef.value.focusSearch(),0<this._actionMatches.length&&(this._selected=this._actionMatches[0]),this.setParent(e.parent)}close(){this._bump=!1,this.visible=!1}setParent(e){this._currentRoot=e||void 0,this._selected=void 0,this._search="",this._headerRef.value.setSearch("")}get breadcrumbs(){var e,t=[];let n=null==(e=this._selected)?void 0:e.parent;if(n)for(t.push(n);n;){const e=this._flatData.find(e=>e.id===n);null!=e&&e.parent&&t.push(e.parent),n=e?e.parent:void 0}return t.reverse()}connectedCallback(){super.connectedCallback(),this.noAutoLoadMdIcons||document.fonts.load("24px Material Icons","apps").then(()=>{}),this._registerInternalHotkeys()}disconnectedCallback(){super.disconnectedCallback(),this._unregisterInternalHotkeys()}_flattern(e,i){let o=[];return(e=e||[]).map(e=>{var t=e.children&&e.children.some(e=>"string"==typeof e),n={...e,parent:e.parent||i};return t||(n.children&&n.children.length&&(i=e.id,o=[...o,...n.children]),n.children=n.children?n.children.map(e=>e.id):[]),n}).concat(o.length?this._flattern(o,i):o)}update(e){e.has("data")&&!this.disableHotkeys&&(this._flatData=this._flattern(this.data),this._flatData.filter(e=>!!e.hotkey).forEach(t=>{H(t.hotkey,e=>{e.preventDefault(),t.handler&&t.handler(t)})})),super.update(e)}_registerInternalHotkeys(){this.openHotkey&&H(this.openHotkey,e=>{e.preventDefault(),this.visible?this.close():this.open()}),this.selectHotkey&&H(this.selectHotkey,e=>{this.visible&&(e.preventDefault(),this._actionSelected(this._actionMatches[this._selectedIndex]))}),this.goBackHotkey&&H(this.goBackHotkey,e=>{!this.visible||this._search||(e.preventDefault(),this._goBack())}),this.navigationDownHotkey&&H(this.navigationDownHotkey,e=>{this.visible&&(e.preventDefault(),this._selectedIndex>=this._actionMatches.length-1?this._selected=this._actionMatches[0]:this._selected=this._actionMatches[this._selectedIndex+1])}),this.navigationUpHotkey&&H(this.navigationUpHotkey,e=>{this.visible&&(e.preventDefault(),0===this._selectedIndex?this._selected=this._actionMatches[this._actionMatches.length-1]:this._selected=this._actionMatches[this._selectedIndex-1])}),this.closeHotkey&&H(this.closeHotkey,()=>{this.visible&&this.close()})}_unregisterInternalHotkeys(){this.openHotkey&&H.unbind(this.openHotkey),this.selectHotkey&&H.unbind(this.selectHotkey),this.goBackHotkey&&H.unbind(this.goBackHotkey),this.navigationDownHotkey&&H.unbind(this.navigationDownHotkey),this.navigationUpHotkey&&H.unbind(this.navigationUpHotkey),this.closeHotkey&&H.unbind(this.closeHotkey)}_actionFocused(e,t){this._selected=e,t.target.ensureInView()}_onTransitionEnd(){this._bump=!1}_goBack(){var e=1<this.breadcrumbs.length?this.breadcrumbs[this.breadcrumbs.length-2]:void 0;this.setParent(e)}render(){var e={bump:this._bump,"modal-content":!0},t={visible:this.visible,modal:!0},n=this._flatData.filter(e=>{var t=new RegExp(this._search,"gi"),n=e.title.match(t)||(null==(n=e.keywords)?void 0:n.match(t));return(!this._currentRoot&&this._search||e.parent===this._currentRoot)&&n}).reduce((e,t)=>e.set(t.section,[...e.get(t.section)||[],t]),new Map);this._actionMatches=[...n.values()].flat(),0<this._actionMatches.length&&-1===this._selectedIndex&&(this._selected=this._actionMatches[0]),0===this._actionMatches.length&&(this._selected=void 0);const i=e=>s` ${Pe(e,e=>e.id,t=>{var e;return s`<ninja-action
            exportparts="ninja-action,ninja-selected,ninja-icon"
            .selected=${Oe(t.id===(null==(e=this._selected)?void 0:e.id))}
            .hotKeysJoinedView=${this.hotKeysJoinedView}
            @mouseover=${e=>this._actionFocused(t,e)}
            @actionsSelected=${e=>this._actionSelected(e.detail)}
            .action=${t}
          ></ninja-action>`})}`,o=[];return n.forEach((e,t)=>{t=t?s`<div class="group-header">${t}</div>`:void 0;o.push(s`${t}${i(e)}`)}),s`
      <div @click=${this._overlayClick} class=${Ke(t)}>
        <div class=${Ke(e)} @animationend=${this._onTransitionEnd}>
          <ninja-header
            exportparts="ninja-input,ninja-input-wrapper"
            ${Te(this._headerRef)}
            .placeholder=${this.placeholder}
            .hideBreadcrumbs=${this.hideBreadcrumbs}
            .breadcrumbs=${this.breadcrumbs}
            @change=${this._handleInput}
            @setParent=${e=>this.setParent(e.detail.parent)}
            @close=${this.close}
          >
          </ninja-header>
          <div class="modal-body">
            <div class="actions-list" part="actions-list">${o}</div>
          </div>
          <slot name="footer"> ${st} </slot>
        </div>
      </div>
    `}get _selectedIndex(){return this._selected?this._actionMatches.indexOf(this._selected):-1}_actionSelected(e){var t;if(this.dispatchEvent(new CustomEvent("selected",{detail:{search:this._search,action:e},bubbles:!0,composed:!0})),e){if(e.children&&0<(null==(t=e.children)?void 0:t.length)&&(this._currentRoot=e.id,this._search=""),this._headerRef.value.setSearch(""),this._headerRef.value.focusSearch(),e.handler){const t=e.handler(e);null!=t&&t.keepOpen||this.close()}this._bump=!0}}async _handleInput(e){this._search=e.detail.search,await this.updateComplete,this.dispatchEvent(new CustomEvent("change",{detail:{search:this._search,actions:this._actionMatches},bubbles:!0,composed:!0}))}_overlayClick(e){null!=(e=e.target)&&e.classList.contains("modal")&&this.close()}};i.styles=[rt],B([a({type:String})],i.prototype,"placeholder",void 0),B([a({type:Boolean})],i.prototype,"disableHotkeys",void 0),B([a({type:Boolean})],i.prototype,"hideBreadcrumbs",void 0),B([a()],i.prototype,"openHotkey",void 0),B([a()],i.prototype,"navigationUpHotkey",void 0),B([a()],i.prototype,"navigationDownHotkey",void 0),B([a()],i.prototype,"closeHotkey",void 0),B([a()],i.prototype,"goBackHotkey",void 0),B([a()],i.prototype,"selectHotkey",void 0),B([a({type:Boolean})],i.prototype,"hotKeysJoinedView",void 0),B([a({type:Boolean})],i.prototype,"noAutoLoadMdIcons",void 0),B([a({type:Array,hasChanged:()=>!0})],i.prototype,"data",void 0),B([E()],i.prototype,"visible",void 0),B([E()],i.prototype,"_bump",void 0),B([E()],i.prototype,"_actionMatches",void 0),B([E()],i.prototype,"_search",void 0),B([E()],i.prototype,"_currentRoot",void 0),B([E()],i.prototype,"_flatData",void 0),B([E()],i.prototype,"breadcrumbs",null),B([E()],i.prototype,"_selected",void 0),B([ge("ninja-keys")],i)}}]);