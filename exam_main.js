var answerlen=document.getElementsByClassName("test-ana").length;
for (var i=0;i<answerlen;i++){
    var rightanswers=document.getElementsByClassName("test-ana")[i].innerText.replace("参考答案：\n","");
    var is_single=document.getElementsByClassName("test-header")[i].innerText;
    if (is_single.indexOf("多选题") != -1){
        var rightanswerlist=rightanswers.split(' ');
        console.log(rightanswerlist);
        for (n = 0; n < rightanswerlist.length; n++) {
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
        var rightanswer=rightanswers
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
       


    
