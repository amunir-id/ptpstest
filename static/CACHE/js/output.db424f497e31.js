(()=>{function l(i){i.directive("dialog",(e,t)=>{t.value==="overlay"?m(e,i):t.value==="panel"?x(e,i):t.value==="title"?w(e,i):t.value==="description"?g(e,i):v(e,i)}),i.magic("dialog",e=>{let t=i.$data(e);return{get open(){return t.__isOpen},get isOpen(){return t.__isOpen},close(){t.__close()}}})}function v(i,e){e.bind(i,{"x-data"(){return{init(){e.bound(i,"open")!==void 0&&e.effect(()=>{this.__isOpenState=e.bound(i,"open")}),e.bound(i,"initial-focus")!==void 0&&this.$watch("__isOpenState",()=>{!this.__isOpenState||setTimeout(()=>{e.bound(i,"initial-focus").focus()},0)})},__isOpenState:!1,__close(){e.bound(i,"open")?this.$dispatch("close"):this.__isOpenState=!1},get __isOpen(){return e.bound(i,"static",this.__isOpenState)}}},"x-modelable":"__isOpenState","x-id"(){return["alpine-dialog-title","alpine-dialog-description"]},"x-show"(){return this.__isOpen},"x-trap.inert.noscroll"(){return this.__isOpen},"@keydown.escape"(){this.__close()},":aria-labelledby"(){return this.$id("alpine-dialog-title")},":aria-describedby"(){return this.$id("alpine-dialog-description")},role:"dialog","aria-modal":"true"})}function m(i,e){e.bind(i,{"x-init"(){this.$data.__isOpen===void 0&&console.warn('"x-dialog:overlay" is missing a parent element with "x-dialog".')},"x-show"(){return this.__isOpen},"@click.prevent.stop"(){this.$data.__close()}})}function x(i,e){e.bind(i,{"@click.outside"(){this.$data.__close()},"x-show"(){return this.$data.__isOpen}})}function w(i,e){e.bind(i,{"x-init"(){this.$data.__isOpen===void 0&&console.warn('"x-dialog:title" is missing a parent element with "x-dialog".')},":id"(){return this.$id("alpine-dialog-title")}})}function g(i,e){e.bind(i,{":id"(){return this.$id("alpine-dialog-description")}})}function u(i){i.directive("disclosure",(e,t)=>{t.value?t.value==="panel"?y(e,i):t.value==="button"&&E(e,i):O(e,i)}),i.magic("disclosure",e=>{let t=i.$data(e);return{get isOpen(){return t.__isOpen},close(){t.__close()}}})}function O(i,e){e.bind(i,{"x-modelable":"__isOpen","x-data"(){return{init(){queueMicrotask(()=>{let t=Boolean(e.bound(this.$el,"default-open",!1));t&&(this.__isOpen=t)})},__isOpen:!1,__close(){this.__isOpen=!1},__toggle(){this.__isOpen=!this.__isOpen}}},"x-id"(){return["alpine-disclosure-panel"]}})}function E(i,e){e.bind(i,{"x-init"(){this.$el.tagName.toLowerCase()==="button"&&!this.$el.hasAttribute("type")&&(this.$el.type="button")},"@click"(){this.$data.__isOpen=!this.$data.__isOpen},":aria-expanded"(){return this.$data.__isOpen},":aria-controls"(){return this.$data.$id("alpine-disclosure-panel")},"@keydown.space.prevent.stop"(){this.$data.__toggle()},"@keydown.enter.prevent.stop"(){this.$data.__toggle()},"@keyup.space.prevent"(){}})}function y(i,e){e.bind(i,{"x-show"(){return this.$data.__isOpen},":id"(){return this.$data.$id("alpine-disclosure-panel")}})}function h(i){i.directive("menu",(e,t)=>{t.value?t.value==="items"?S(e,i):t.value==="item"?N(e,i):t.value==="button"&&D(e,i):k(e,i)}),i.magic("menuItem",e=>{let t=i.$data(e);return{get isActive(){return t.__activeEl==t.__itemEl},get isDisabled(){return e.__isDisabled.value}}})}function k(i,e){e.bind(i,{"x-id"(){return["alpine-menu-button","alpine-menu-items"]},"x-modelable":"__isOpen","x-data"(){return{__itemEls:[],__activeEl:null,__isOpen:!1,__open(){this.__isOpen=!0,(s=>requestAnimationFrame(()=>requestAnimationFrame(s)))(()=>this.$refs.__items.focus({preventScroll:!0}))},__close(t=!0){this.__isOpen=!1,t&&this.$nextTick(()=>this.$refs.__button.focus({preventScroll:!0}))},__contains(t,s){return!!e.findClosest(s,a=>a.isSameNode(t))}}},"@focusin.window"(){this.$data.__contains(this.$el,document.activeElement)||this.$data.__close(!1)}})}function D(i,e){e.bind(i,{"x-ref":"__button","aria-haspopup":"true",":aria-labelledby"(){return this.$id("alpine-menu-label")},":id"(){return this.$id("alpine-menu-button")},":aria-expanded"(){return this.$data.__isOpen},":aria-controls"(){return this.$data.__isOpen&&this.$id("alpine-menu-items")},"x-init"(){this.$el.tagName.toLowerCase()==="button"&&!this.$el.hasAttribute("type")&&(this.$el.type="button")},"@click"(){this.$data.__open()},"@keydown.down.stop.prevent"(){this.$data.__open()},"@keydown.up.stop.prevent"(){this.$data.__open(_.Alpine,last)},"@keydown.space.stop.prevent"(){this.$data.__open()},"@keydown.enter.stop.prevent"(){this.$data.__open()}})}function S(i,e){e.bind(i,{"x-ref":"__items","aria-orientation":"vertical",role:"menu",":id"(){return this.$id("alpine-menu-items")},":aria-labelledby"(){return this.$id("alpine-menu-button")},":aria-activedescendant"(){return this.$data.__activeEl&&this.$data.__activeEl.id},"x-show"(){return this.$data.__isOpen},tabindex:"0","@click.outside"(){this.$data.__close()},"@keydown"(t){_.search(e,this.$refs.__items,t.key,s=>s.__activate())},"@keydown.down.stop.prevent"(){this.$data.__activeEl?_.next(e,this.$data.__activeEl,t=>t.__activate()):_.first(e,this.$refs.__items,t=>t.__activate())},"@keydown.up.stop.prevent"(){this.$data.__activeEl?_.previous(e,this.$data.__activeEl,t=>t.__activate()):_.last(e,this.$refs.__items,t=>t.__activate())},"@keydown.home.stop.prevent"(){_.first(e,this.$refs.__items,t=>t.__activate())},"@keydown.end.stop.prevent"(){_.last(e,this.$refs.__items,t=>t.__activate())},"@keydown.page-up.stop.prevent"(){_.first(e,this.$refs.__items,t=>t.__activate())},"@keydown.page-down.stop.prevent"(){_.last(e,this.$refs.__items,t=>t.__activate())},"@keydown.escape.stop.prevent"(){this.$data.__close()},"@keydown.space.stop.prevent"(){this.$data.__activeEl&&this.$data.__activeEl.click()},"@keydown.enter.stop.prevent"(){this.$data.__activeEl&&this.$data.__activeEl.click()},"@keyup.space.prevent"(){}})}function N(i,e){e.bind(i,()=>({"x-data"(){return{__itemEl:this.$el,init(){let t=e.raw(this.$data.__itemEls),s=!1;for(let a=0;a<t.length;a++)if(t[a].compareDocumentPosition(this.$el)&Node.DOCUMENT_POSITION_PRECEDING){t.splice(a,0,this.$el),s=!0;break}s||t.push(this.$el),this.$el.__activate=()=>{this.$data.__activeEl=this.$el,this.$el.scrollIntoView({block:"nearest"})},this.$el.__deactivate=()=>{this.$data.__activeEl=null},this.$el.__isDisabled=e.reactive({value:!1}),queueMicrotask(()=>{this.$el.__isDisabled.value=e.bound(this.$el,"disabled",!1)})},destroy(){let t=this.$data.__itemEls;t.splice(t.indexOf(this.$el),1)}}},"x-id"(){return["alpine-menu-item"]},":id"(){return this.$id("alpine-menu-item")},":tabindex"(){return this.$el.__isDisabled.value?!1:"-1"},role:"menuitem","@mousemove"(){this.$el.__isDisabled.value||this.$menuItem.isActive||this.$el.__activate()},"@mouseleave"(){this.$el.__isDisabled.value||!this.$menuItem.isActive||this.$el.__deactivate()}}))}var _={first(i,e,t=a=>a,s=()=>{}){let a=i.$data(e).__itemEls[0];return a?a.tagName.toLowerCase()==="template"?this.next(i,a,t):a.__isDisabled.value?this.next(i,a,t):t(a):s()},last(i,e,t=a=>a,s=()=>{}){let a=i.$data(e).__itemEls.slice(-1)[0];return a?a.__isDisabled.value?this.previous(i,a,t):t(a):s()},next(i,e,t=a=>a,s=()=>{}){if(!e)return s();let a=i.$data(e).__itemEls,n=a[a.indexOf(e)+1];return n?n.__isDisabled.value||n.tagName.toLowerCase()==="template"?this.next(i,n,t,s):t(n):s()},previous(i,e,t=a=>a,s=()=>{}){if(!e)return s();let a=i.$data(e).__itemEls,n=a[a.indexOf(e)-1];return n?n.__isDisabled.value||n.tagName.toLowerCase()==="template"?this.previous(i,n,t,s):t(n):s()},searchQuery:"",debouncedClearSearch:void 0,clearSearch(i){this.debouncedClearSearch||(this.debouncedClearSearch=i.debounce(function(){this.searchQuery=""},350)),this.debouncedClearSearch()},search(i,e,t,s){if(t.length>1)return;this.searchQuery+=t;let n=i.raw(i.$data(e).__itemEls).find(o=>o.textContent.trim().toLowerCase().startsWith(this.searchQuery));n&&!n.__isDisabled.value&&s(n),this.clearSearch(i)}};function c(i){i.directive("switch",(e,t)=>{t.value==="group"?T(e,i):t.value==="label"?L(e,i):t.value==="description"?C(e,i):I(e,i)}),i.magic("switch",e=>{let t=i.$data(e);return{get isChecked(){return t.__value===!0}}})}function T(i,e){e.bind(i,{"x-id"(){return["alpine-switch-label","alpine-switch-description"]},"x-data"(){return{__hasLabel:!1,__hasDescription:!1,__switchEl:void 0}}})}function I(i,e){e.bind(i,{"x-modelable":"__value","x-data"(){return{init(){queueMicrotask(()=>{this.__value=e.bound(this.$el,"default-checked",!1),this.__inputName=e.bound(this.$el,"name",!1),this.__inputValue=e.bound(this.$el,"value","on"),this.__inputId="alpine-switch-"+Date.now()})},__value:void 0,__inputName:void 0,__inputValue:void 0,__inputId:void 0,__toggle(){this.__value=!this.__value}}},"x-effect"(){let t=this.__value;if(!this.__inputName)return;let s=this.$el.nextElementSibling;if(s&&String(s.id)===String(this.__inputId)&&s.remove(),t){let a=document.createElement("input");a.type="hidden",a.value=this.__inputValue,a.name=this.__inputName,a.id=this.__inputId,this.$el.after(a)}},"x-init"(){this.$el.tagName.toLowerCase()==="button"&&!this.$el.hasAttribute("type")&&(this.$el.type="button"),this.$data.__switchEl=this.$el},role:"switch",tabindex:"0",":aria-checked"(){return!!this.__value},":aria-labelledby"(){return this.$data.__hasLabel&&this.$id("alpine-switch-label")},":aria-describedby"(){return this.$data.__hasDescription&&this.$id("alpine-switch-description")},"@click.prevent"(){this.__toggle()},"@keyup"(t){t.key!=="Tab"&&t.preventDefault(),t.key===" "&&this.__toggle()},"@keypress.prevent"(){}})}function L(i,e){e.bind(i,{"x-init"(){this.$data.__hasLabel=!0},":id"(){return this.$id("alpine-switch-label")},"@click"(){this.$data.__switchEl.click(),this.$data.__switchEl.focus({preventScroll:!0})}})}function C(i,e){e.bind(i,{"x-init"(){this.$data.__hasDescription=!0},":id"(){return this.$id("alpine-switch-description")}})}function p(i){i.directive("popover",(e,t)=>{t.value?t.value==="overlay"?R(e,i):t.value==="button"?F(e,i):t.value==="panel"?V(e,i):t.value==="group"&&M(e,i):P(e,i)}),i.magic("popover",e=>{let t=i.$data(e);return{get isOpen(){return t.__isOpenState},open(){t.__open()},close(){t.__close()}}})}function P(i,e){e.bind(i,{"x-id"(){return["alpine-popover-button","alpine-popover-panel"]},"x-modelable":"__isOpenState","x-data"(){return{init(){this.$data.__groupEl&&this.$data.__groupEl.addEventListener("__close-others",({detail:t})=>{t.el.isSameNode(this.$el)||this.__close(!1)})},__buttonEl:void 0,__panelEl:void 0,__isStatic:!1,get __isOpen(){return this.__isStatic?!0:this.__isOpenState},__isOpenState:!1,__open(){this.__isOpenState=!0,this.$dispatch("__close-others",{el:this.$el})},__toggle(){this.__isOpenState?this.__close():this.__open()},__close(t){this.__isStatic||(this.__isOpenState=!1,t!==!1&&(t=t||this.$data.__buttonEl,!document.activeElement.isSameNode(t)&&setTimeout(()=>t.focus())))},__contains(t,s){return!!e.findClosest(s,a=>a.isSameNode(t))}}},"@keydown.escape.stop.prevent"(){this.__close()},"@focusin.window"(){if(this.$data.__groupEl){this.$data.__contains(this.$data.__groupEl,document.activeElement)||this.$data.__close(!1);return}this.$data.__contains(this.$el,document.activeElement)||this.$data.__close(!1)}})}function F(i,e){e.bind(i,{"x-ref":"button",":id"(){return this.$id("alpine-popover-button")},":aria-expanded"(){return this.$data.__isOpen},":aria-controls"(){return this.$data.__isOpen&&this.$id("alpine-popover-panel")},"x-init"(){this.$el.tagName.toLowerCase()==="button"&&!this.$el.hasAttribute("type")&&(this.$el.type="button"),this.$data.__buttonEl=this.$el},"@click"(){this.$data.__toggle()},"@keydown.tab"(t){if(!t.shiftKey&&this.$data.__isOpen){let s=this.$focus.within(this.$data.__panelEl).getFirst();s&&(t.preventDefault(),t.stopPropagation(),this.$focus.focus(s))}},"@keyup.tab"(t){if(this.$data.__isOpen){let s=this.$focus.previouslyFocused();if(!s)return;!this.$data.__buttonEl.contains(s)&&!this.$data.__panelEl.contains(s)&&s&&this.$el.compareDocumentPosition(s)&Node.DOCUMENT_POSITION_FOLLOWING&&(t.preventDefault(),t.stopPropagation(),this.$focus.within(this.$data.__panelEl).last())}},"@keydown.space.stop.prevent"(){this.$data.__toggle()},"@keydown.enter.stop.prevent"(){this.$data.__toggle()},"@keyup.space.stop.prevent"(){}})}function V(i,e){e.bind(i,{"x-init"(){this.$data.__isStatic=e.bound(this.$el,"static",!1),this.$data.__panelEl=this.$el},"x-effect"(){this.$data.__isOpen&&e.bound(i,"focus")&&this.$focus.first()},"x-ref":"panel",":id"(){return this.$id("alpine-popover-panel")},"x-show"(){return this.$data.__isOpen},"@mousedown.window"(t){!this.$data.__isOpen||this.$data.__contains(this.$data.__buttonEl,t.target)||this.$data.__contains(this.$el,t.target)||this.$focus.focusable(t.target)||this.$data.__close()},"@keydown.tab"(t){if(t.shiftKey&&this.$focus.isFirst(t.target))t.preventDefault(),t.stopPropagation(),e.bound(i,"focus")?this.$data.__close():this.$data.__buttonEl.focus();else if(!t.shiftKey&&this.$focus.isLast(t.target)){t.preventDefault(),t.stopPropagation();let s=this.$focus.within(document).all(),a=s.indexOf(this.$data.__buttonEl);s.splice(a+1).filter(o=>!this.$el.contains(o))[0].focus(),e.bound(i,"focus")&&this.$data.__close(!1)}}})}function M(i,e){e.bind(i,{"x-ref":"container","x-data"(){return{__groupEl:this.$el}}})}function R(i,e){e.bind(i,{"x-show"(){return this.$data.__isOpen}})}function f(i){i.directive("radio",(e,t)=>{t.value?t.value==="option"?q(e,i):t.value==="label"?W(e,i):t.value==="description"&&G(e,i):B(e,i)}),i.magic("radioOption",e=>{let t=i.$data(e);return{get isActive(){return t.__option===t.__active},get isChecked(){return t.__option===t.__value},get isDisabled(){let s=t.__disabled;return t.__rootDisabled?!0:s}}})}function B(i,e){e.bind(i,{"x-modelable":"__value","x-data"(){return{init(){queueMicrotask(()=>{this.__rootDisabled=e.bound(i,"disabled",!1),this.__value=e.bound(this.$el,"default-value",!1),this.__inputName=e.bound(this.$el,"name",!1),this.__inputId="alpine-radio-"+Date.now()}),this.$nextTick(()=>{let t=document.createTreeWalker(this.$el,NodeFilter.SHOW_ELEMENT,{acceptNode:s=>s.getAttribute("role")==="radio"?NodeFilter.FILTER_REJECT:s.hasAttribute("role")?NodeFilter.FILTER_SKIP:NodeFilter.FILTER_ACCEPT},!1);for(;t.nextNode();)t.currentNode.setAttribute("role","none")})},__value:void 0,__active:void 0,__rootEl:this.$el,__optionValues:[],__disabledOptions:new Set,__optionElsByValue:new Map,__hasLabel:!1,__hasDescription:!1,__rootDisabled:!1,__inputName:void 0,__inputId:void 0,__change(t){this.__rootDisabled||(this.__value=t)},__addOption(t,s,a){let n=e.raw(this.__optionValues),o=n.map(d=>this.__optionElsByValue.get(d)),r=!1;for(let d=0;d<o.length;d++)if(o[d].compareDocumentPosition(s)&Node.DOCUMENT_POSITION_PRECEDING){n.splice(d,0,t),this.__optionElsByValue.set(t,s),r=!0;break}r||(n.push(t),this.__optionElsByValue.set(t,s)),a&&this.__disabledOptions.add(t)},__isFirstOption(t){return this.__optionValues.indexOf(t)===0},__setActive(t){this.__active=t},__focusOptionNext(){let t=this.__active,s=this.__optionValues.filter(n=>!this.__disabledOptions.has(n)),a=s[this.__optionValues.indexOf(t)+1];a=a||s[0],this.__optionElsByValue.get(a).focus(),this.__change(a)},__focusOptionPrev(){let t=this.__active,s=this.__optionValues.filter(n=>!this.__disabledOptions.has(n)),a=s[s.indexOf(t)-1];a=a||s.slice(-1)[0],this.__optionElsByValue.get(a).focus(),this.__change(a)}}},"x-effect"(){let t=this.__value;if(!this.__inputName)return;let s=this.$el.nextElementSibling;if(s&&String(s.id)===String(this.__inputId)&&s.remove(),t){let a=document.createElement("input");a.type="hidden",a.value=t,a.name=this.__inputName,a.id=this.__inputId,this.$el.after(a)}},role:"radiogroup","x-id"(){return["alpine-radio-label","alpine-radio-description"]},":aria-labelledby"(){return this.__hasLabel&&this.$id("alpine-radio-label")},":aria-describedby"(){return this.__hasDescription&&this.$id("alpine-radio-description")},"@keydown.up.prevent.stop"(){this.__focusOptionPrev()},"@keydown.left.prevent.stop"(){this.__focusOptionPrev()},"@keydown.down.prevent.stop"(){this.__focusOptionNext()},"@keydown.right.prevent.stop"(){this.__focusOptionNext()}})}function q(i,e){e.bind(i,{"x-data"(){return{init(){queueMicrotask(()=>{this.__disabled=e.bound(i,"disabled",!1),this.__option=e.bound(i,"value"),this.$data.__addOption(this.__option,this.$el,this.__disabled)})},__option:void 0,__disabled:!1,__hasLabel:!1,__hasDescription:!1}},"x-id"(){return["alpine-radio-label","alpine-radio-description"]},role:"radio",":aria-checked"(){return this.$radioOption.isChecked},":aria-disabled"(){return this.$radioOption.isDisabled},":aria-labelledby"(){return this.__hasLabel&&this.$id("alpine-radio-label")},":aria-describedby"(){return this.__hasDescription&&this.$id("alpine-radio-description")},":tabindex"(){return this.$radioOption.isDisabled?-1:this.$radioOption.isChecked||!this.$data.__value&&this.$data.__isFirstOption(this.$data.__option)?0:-1},"@click"(){this.$radioOption.isDisabled||(this.$data.__change(this.$data.__option),this.$el.focus())},"@focus"(){this.$radioOption.isDisabled||this.$data.__setActive(this.$data.__option)},"@blur"(){this.$data.__active===this.$data.__option&&this.$data.__setActive(void 0)},"@keydown.space.stop.prevent"(){this.$data.__change(this.$data.__option)}})}function W(i,e){e.bind(i,{"x-init"(){this.$data.__hasLabel=!0},":id"(){return this.$id("alpine-radio-label")}})}function G(i,e){e.bind(i,{"x-init"(){this.$data.__hasDescription=!0},":id"(){return this.$id("alpine-radio-description")}})}function $(i){i.directive("tabs",(e,t)=>{t.value?t.value==="list"?Q(e,i):t.value==="tab"?U(e,i):t.value==="panels"?j(e,i):t.value==="panel"&&H(e,i):K(e,i)}),i.magic("tab",e=>{let t=i.$data(e);return{get isSelected(){return t.__selectedIndex===t.__tabs.indexOf(t.__tabEl)},get isDisabled(){return t.__isDisabled}}}),i.magic("panel",e=>{let t=i.$data(e);return{get isSelected(){return t.__selectedIndex===t.__panels.indexOf(t.__panelEl)}}})}function K(i,e){e.bind(i,{"x-modelable":"__selectedIndex","x-data"(){return{init(){queueMicrotask(()=>{let t=this.__selectedIndex||Number(e.bound(this.$el,"default-index",0)),s=this.__activeTabs(),a=(n,o,r)=>Math.min(Math.max(n,o),r);this.__selectedIndex=a(t,0,s.length-1),e.effect(()=>{this.__manualActivation=e.bound(this.$el,"manual",!1)})})},__tabs:[],__panels:[],__selectedIndex:null,__tabGroupEl:void 0,__manualActivation:!1,__addTab(t){this.__tabs.push(t)},__addPanel(t){this.__panels.push(t)},__selectTab(t){this.__selectedIndex=this.__tabs.indexOf(t)},__activeTabs(){return this.__tabs.filter(t=>!t.__disabled)}}}})}function Q(i,e){e.bind(i,{"x-init"(){this.$data.__tabGroupEl=this.$el}})}function U(i,e){e.bind(i,{"x-init"(){this.$el.tagName.toLowerCase()==="button"&&!this.$el.hasAttribute("type")&&(this.$el.type="button")},"x-data"(){return{init(){this.__tabEl=this.$el,this.$data.__addTab(this.$el),this.__tabEl.__disabled=e.bound(this.$el,"disabled",!1),this.__isDisabled=this.__tabEl.__disabled},__tabEl:void 0,__isDisabled:!1}},"@click"(){this.$el.__disabled||(this.$data.__selectTab(this.$el),this.$el.focus())},"@keydown.enter.prevent.stop"(){this.__selectTab(this.$el)},"@keydown.space.prevent.stop"(){this.__selectTab(this.$el)},"@keydown.home.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).first()},"@keydown.page-up.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).first()},"@keydown.end.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).last()},"@keydown.page-down.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).last()},"@keydown.down.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).withWrapAround().next()},"@keydown.right.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).withWrapAround().next()},"@keydown.up.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).withWrapAround().prev()},"@keydown.left.prevent.stop"(){this.$focus.within(this.$data.__activeTabs()).withWrapAround().prev()},":tabindex"(){return this.$tab.isSelected?0:-1},"@focus"(){if(this.$data.__manualActivation)this.$el.focus();else{if(this.$el.__disabled)return;this.$data.__selectTab(this.$el),this.$el.focus()}}})}function j(i,e){e.bind(i,{})}function H(i,e){e.bind(i,{":tabindex"(){return this.$panel.isSelected?0:-1},"x-data"(){return{init(){this.__panelEl=this.$el,this.$data.__addPanel(this.$el)},__panelEl:void 0}},"x-show"(){return this.$panel.isSelected}})}function b(i){l(i),u(i),h(i),c(i),p(i),f(i),$(i)}document.addEventListener("alpine:init",()=>{window.Alpine.plugin(b)});})();;