document.addEventListener('DOMContentLoaded', function() {
    var timberElement = document.getElementById('timer');
    if (!timberElement) return;

    // 获取日期字符串，优先从 data-time 属性中获取
    var dateString = timberElement.getAttribute('data-time');
    if (!dateString) {
        dateString = timberElement.innerText;
    }

    // 将日期字符串解析为 Date 对象
    var countDownDate = new Date(dateString);
    if (isNaN(countDownDate)) {
        // 日期解析失败，显示错误信息
        timberElement.innerText = "日期格式错误";
        return;
    }

    // 开始倒计时
    var x = setInterval(function() {
        var now = new Date().getTime();
        var distance = countDownDate - now;

        if (distance <= 0) {
            clearInterval(x);
            timberElement.innerText = "倒计时结束";
            return;
        }

        // 计算剩余的天、小时、分钟、秒
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 *60 *24)) / (1000 *60 *60));
        var minutes = Math.floor((distance % (1000 *60 *60)) / (1000 *60));
        var seconds = Math.floor((distance % (1000 *60)) / 1000);

        // 更新页面显示
        timberElement.innerText = days + "天 " + hours + "时 " + minutes + "分 " + seconds + "秒";
    }, 1000);
});