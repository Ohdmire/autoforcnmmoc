import asyncio
from playwright.async_api import async_playwright


js = r"""
    ah.proxy({
    //请求发起前进入
    onRequest: (config, handler) => {
        console.log(config.url)
        handler.next(config);
    },
    //请求发生错误时进入，比如超时；注意，不包括http状态码错误，如404仍然会认为请求成功
    onError: (err, handler) => {
        console.log(err.type)
        handler.next(err)
    },
    //请求成功后进入
    onResponse: (response, handler) => {
        var res=response.response
        response.response=res.replace("var answerReviewTypeFlag = (answerReviewType == 2 && submitFlag == 1);","var answerReviewTypeFlag = true")
        console.log(response.response)
        handler.next(response)
    }
})
"""

ajaxhookjs = r'!function(t,e){for(var r in e)t[r]=e[r]}(window,function(t){function e(n){if(r[n])return r[n].exports;var o=r[n]={i:n,l:!1,exports:{}};return t[n].call(o.exports,o,o.exports,e),o.l=!0,o.exports}var r={};return e.m=t,e.c=r,e.i=function(t){return t},e.d=function(t,r,n){e.o(t,r)||Object.defineProperty(t,r,{configurable:!1,enumerable:!0,get:n})},e.n=function(t){var r=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(r,"a",r),r},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="",e(e.s=3)}([function(t,e,r){"use strict";function n(t,e){var r={};for(var n in t)r[n]=t[n];return r.target=r.currentTarget=e,r}function o(t,e){function r(e){return function(){var r=this[u][e];if(v){var n=this.hasOwnProperty(e+"_")?this[e+"_"]:r,o=(t[e]||{}).getter;return o&&o(n,this)||n}return r}}function o(e){return function(r){var o=this[u];if(v){var i=this,s=t[e];if("on"===e.substring(0,2))i[e+"_"]=r,o[e]=function(s){s=n(s,i),t[e]&&t[e].call(i,o,s)||r.call(i,s)};else{var a=(s||{}).setter;r=a&&a(r,i)||r,this[e+"_"]=r;try{o[e]=r}catch(t){}}}else o[e]=r}}function a(e){return function(){var r=[].slice.call(arguments);if(t[e]&&v){var n=t[e].call(this,r,this[u]);if(n)return n}return this[u][e].apply(this[u],r)}}function c(){v=!1,e.XMLHttpRequest===h&&(e.XMLHttpRequest=f,h.prototype.constructor=f,f=void 0)}e=e||window;var f=e.XMLHttpRequest,v=!0,h=function(){for(var t=new f,e=0;e<s.length;++e){var n="on"+s[e];void 0===t[n]&&(t[n]=null)}for(var c in t){var v="";try{v=i(t[c])}catch(t){}"function"===v?this[c]=a(c):c!==u&&Object.defineProperty(this,c,{get:r(c),set:o(c),enumerable:!0})}var h=this;t.getProxy=function(){return h},this[u]=t};return h.prototype=f.prototype,h.prototype.constructor=h,e.XMLHttpRequest=h,Object.assign(e.XMLHttpRequest,{UNSENT:0,OPENED:1,HEADERS_RECEIVED:2,LOADING:3,DONE:4}),{originXhr:f,unHook:c}}Object.defineProperty(e,"__esModule",{value:!0});var i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t};e.configEvent=n,e.hook=o;var s=e.events=["load","loadend","timeout","error","readystatechange","abort"],u="__origin_xhr"},function(t,e,r){"use strict";function n(t,e){return e=e||window,c(t,e)}function o(t){return t.replace(/^\s+|\s+$/g,"")}function i(t){return t.watcher||(t.watcher=document.createElement("a"))}function s(t,e){var r=t.getProxy(),n="on"+e+"_",o=(0,f.configEvent)({type:e},r);r[n]&&r[n](o);var s;"function"==typeof Event?s=new Event(e,{bubbles:!1}):(s=document.createEvent("Event"),s.initEvent(e,!1,!0)),i(t).dispatchEvent(s)}function u(t){this.xhr=t,this.xhrProxy=t.getProxy()}function a(t){function e(t){u.call(this,t)}return e[x]=Object.create(u[x]),e[x].next=t,e}function c(t,e){function r(t){var e=t.responseType;if(!e||"text"===e)return t.responseText;var r=t.response;if("json"===e&&!r)try{return JSON.parse(t.responseText)}catch(t){console.warn(t)}return r}function n(t,e){var n=new b(t),i={response:r(e),status:e.status,statusText:e.statusText,config:t.config,headers:t.resHeader||t.getAllResponseHeaders().split("\r\n").reduce(function(t,e){if(""===e)return t;var r=e.split(":");return t[r.shift()]=o(r.join(":")),t},{})};if(!x)return n.resolve(i);x(i,n)}function u(t,e,r,n){var o=new w(t);r={config:t.config,error:r,type:n},E?E(r,o):o.next(r)}function a(){return!0}function c(t){return function(e,r){return u(e,this,r,t),!0}}function v(t,e){return 4===t.readyState&&0!==t.status?n(t,e):4!==t.readyState&&s(t,l),!0}var h=t.onRequest,x=t.onResponse,E=t.onError,m=(0,f.hook)({onload:a,onloadend:a,onerror:c(d),ontimeout:c(p),onabort:c(y),onreadystatechange:function(t){return v(t,this)},open:function(t,e){var r=this,n=e.config={headers:{}};n.method=t[0],n.url=t[1],n.async=t[2],n.user=t[3],n.password=t[4],n.xhr=e;var o="on"+l;if(e[o]||(e[o]=function(){return v(e,r)}),h)return!0},send:function(t,e){var r=e.config;if(r.withCredentials=e.withCredentials,r.body=t[0],h){var n=function(){h(r,new g(e))};return!1===r.async?n():setTimeout(n),!0}},setRequestHeader:function(t,e){if(e.config.headers[t[0].toLowerCase()]=t[1],h)return!0},addEventListener:function(t,e){var r=this;if(-1!==f.events.indexOf(t[0])){var n=t[1];return i(e).addEventListener(t[0],function(e){var o=(0,f.configEvent)(e,r);o.type=t[0],o.isTrusted=!0,n.call(r,o)}),!0}},getAllResponseHeaders:function(t,e){var r=e.resHeader;if(r){var n="";for(var o in r)n+=o+": "+r[o]+"\r\n";return n}},getResponseHeader:function(t,e){var r=e.resHeader;if(r)return r[(t[0]||"").toLowerCase()]}},e);return{originXhr:m.originXhr,unProxy:m.unHook}}Object.defineProperty(e,"__esModule",{value:!0}),e.proxy=n;var f=r(0),v=f.events[0],h=f.events[1],p=f.events[2],d=f.events[3],l=f.events[4],y=f.events[5],x="prototype";u[x]=Object.create({resolve:function(t){var e=this.xhrProxy,r=this.xhr;e.readyState=4,r.resHeader=t.headers,e.response=e.responseText=t.response,e.statusText=t.statusText,e.status=t.status,s(r,l),s(r,v),s(r,h)},reject:function(t){this.xhrProxy.status=0,s(this.xhr,t.type),s(this.xhr,h)}});var g=a(function(t){var e=this.xhr;t=t||e.config,e.withCredentials=t.withCredentials,e.open(t.method,t.url,!1!==t.async,t.user,t.password);for(var r in t.headers)e.setRequestHeader(r,t.headers[r]);e.send(t.body)}),b=a(function(t){this.resolve(t)}),w=a(function(t){this.reject(t)})},,function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.ah=void 0;var n=r(0),o=r(1);e.ah={proxy:o.proxy,hook:n.hook}}]));'

select_answer_js=r"""
var answerlen=document.getElementsByClassName("test-ana").length;
for (var i=0;i<answerlen;i++){
    var rightanswers=document.getElementsByClassName("test-ana")[i].innerText.replace("参考答案：\n","");
    var is_single=document.getElementsByClassName("test-header")[i].innerText;
    if (is_single.indexOf("多选题") != -1){
        var rightanswerlist=rightanswers.split(' ');
        console.log(rightanswerlist);
        for (var n = 0; n < rightanswerlist.length; n++) {
            var rightanswer=rightanswerlist[n];

            if (rightanswer=="A")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[0].getElementsByClassName("input-c")[0].click();
            }
            else if (rightanswer=="B")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[1].getElementsByClassName("input-c")[0].click();
            }
            else if (rightanswer=="C")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[2].getElementsByClassName("input-c")[0].click();
            }
            else if (rightanswer=="D")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[3].getElementsByClassName("input-c")[0].click();
            }
            else if (rightanswer=="E")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[4].getElementsByClassName("input-c")[0].click();
            }
            else if (rightanswer=="F")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[5].getElementsByClassName("input-c")[0].click();
            }
            else
            {
                alert("未找到答案");
            }
            }
    }
    else{
        rightanswer=rightanswers
        if (rightanswer=="A")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[0].getElementsByClassName("input-r")[0].click();
            }
            else if (rightanswer=="B")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[1].getElementsByClassName("input-r")[0].click();
            }
            else if (rightanswer=="C")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[2].getElementsByClassName("input-r")[0].click();
            }
            else if (rightanswer=="D")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[3].getElementsByClassName("input-r")[0].click();
            }
            else if (rightanswer=="E")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[4].getElementsByClassName("input-r")[0].click();
            }
            else if (rightanswer=="F")
            {
                document.getElementsByClassName("test-ana")[i].parentElement.getElementsByClassName("t-option")[5].getElementsByClassName("input-r")[0].click();
            }
            else
            {
                alert("未找到答案");
            }
    }

}
       
"""

url="http://180.76.151.202"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,channel="msedge")
        context = await browser.new_context()#storage_state="cookies.json"
        page = await context.new_page()
        await page.goto(url)
        input("请进入**章节导航**后，按回车键继续")
    # 保存cookie信息到文件
        # await context.storage_state(path="cookies.json")
        await page.wait_for_selector('.lecture-action')
        elements = await page.locator('.lecture-action').all()
        for element in elements:
            html=await element.inner_html()
            text=await element.inner_text()
            if "icon-edit-done" in html:
                print("已完成"+text)
            else:
                print("未完成"+text)
                if "play" in html:
                    print("非练习"+text+"跳过")
                else:
                    print("视频未看完，即将开始播放"+"\n"+text+"\n")
                    await element.click()
                    await page.wait_for_selector('#enterObjectExamDiv')
                    #加载js
                    await page.evaluate(ajaxhookjs)
                    await page.evaluate(js)
                    if await page.is_visible('.doObjExam'):
                        await page.locator(".doObjExam").click()
                    else:
                        await page.locator(".enter_exam").click()
                    await asyncio.sleep(1)
                    #选择答案部分
                    await page.evaluate(select_answer_js)
                    await asyncio.sleep(1)
                    await page.click('#submit_exam')
                    if "未做" in await page.locator(".d-content").text_content():
                        print("未做"+text+"跳过")
                        await page.go_back()
                        continue
                    else:
                        await page.locator(".d-button").get_by_text("坚持提交").click()
                    print("练习已完成"+"\n"+text+"\n")
                    await page.go_back()
        input("程序执行完毕，按回车键退出")

asyncio.run(main())