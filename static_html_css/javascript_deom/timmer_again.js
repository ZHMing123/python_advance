// 声明一个全局的t, 保存定时器的ID
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

// 点击开始按钮，让时间滚动起来
// 找到开始按钮，给它绑定事件
var startButton = document.getElementById("start");
startButton.onclick = function () {
    foo();
    // 每隔1秒执行一次foo
    if (t === undefined) {
        t = setInterval(foo, 1000);  // 把定时器的id复制给t
    }
};

// 点击停止按钮，让时间停止
// 找到停止按钮，给它绑定事件
var stopButton = document.getElementById("stop");
stopButton.onclick = function () {
    // 清除之前设置的定时器
    clearInterval(t);  // 清除t对应的定时器，t的值还在
    console.log(t);
    t = undefined;
};
