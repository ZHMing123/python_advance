// 声明一个全局的t，保存定时器的ID
var t;

// 在input框里显示当前时间
// 1、获取当前时间
function foo() {
    var now = new Date();
    var nowStr = now.toLocaleString();
    // 2、把时间字符串填到input框里
    var timmerEle = document.getElementById("timmer");
    timmerEle.value = nowStr;
}

// 点击开始让时间动起来
// 找到开始按钮，给它绑定事件
var startButton = document.getElementById("start");
startButton.onclick = function () {
    foo();
    // 每隔一秒执行一次foo()
    if (t === undefined) {
        t = setInterval(foo, 1000);

    }
};


// 点击停止
// 找到停止按钮，给它绑定事件
var stopButton = document.getElementById("stop");
stopButton.onclick = function () {
    // 清楚之前设置的定时器
    clearInterval(t);
    console.log(t);  // 定时器清除了，t的值还在
    t = undefined;
};

