
host = window.location.host;

hwnd_windows = "/api/tool/hwnd";

api_tool_capture = "/api/tool/capture";

api_tool_capture_list = "/api/tool/capture/list";

fun_findcolors = "/api/fun/findcolors"

fun_findimages = "/api/fun/findimages"

fun_findocr = "/api/fun/ocr"

fun_comparecolors = "/api/fun/comparecolors"

model_list = "/api/model/list"





$(document).ready(function () {
    var path = window.location.pathname
    switch (path) {
        case "":
        case "/":
            $("#nav_li_home").addClass("active")
            break;
        case "/hwnd":
            $("#nav_li_hwnd").addClass("active")
            break;
        case "/colors":
            $("#nav_li_colors").addClass("active")
            break;
    }
})