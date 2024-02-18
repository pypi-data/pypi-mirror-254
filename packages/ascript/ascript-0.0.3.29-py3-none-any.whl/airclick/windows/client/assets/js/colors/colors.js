// const baseUrl = 'http://192.168.31.58:9096'
const captureDir = "/sdcard/airscript/screen/capture/"
const screenTempDir = "/sdcard/airscript/screen/temp/"
const uploadDir = "/sdcard/airscript/screen/upload/"
const moduleDir = "/sdcard/airscript/model/"
var image = document.getElementById('img_preview');
var image_data_object;
var info_XY= $("#header_cur_xy");
var info_RGB = $("#header_cur_rgb");
var info_color = $("#header_cur_colrshow");
var conimg = $("#container_img");
var part_box = $("#part_box");
var pos_mouse_down = {};
var mouse_move_xyc = {};
var is_mouse_downed = false;
var is_image_mouseover = false;
var x_mouse_down = -1;
var y_mouse_down = -1;
var is_show_box = false;
var scope_pos = [null, null];
var p1 = $("#header_rect");
var img_deleft_dom = null;
var menus = ["#btn_findcolor","#btn_comparecolor","#btn_ocr","#btn_findimage"]

// var imglist = null;

window.onload = function (e) {
    
    getImgList(false);
    image.onload = function () {
        $("#image_loading").hide();
        image_data_object = getImageData();
        $(conimg).scrollLeft(0)
        $(conimg).scrollTop(0)

        $('#header_pixels').text(`${image.width} x ${image.height}`)
        $(".zoomWindow").css("background-size",`${image.width}px ${image.height}px`)
        if (image.height > image.width) {
            $(image).css("height","100%" );
            $(image).css("width", "auto");
        } else {
            $(image).css("width", "100%");
            $(image).css("height", "auto");
        }
    }

    $("#toolbar_img_capture").click(function(e){
        getImgList(true);
    });

    $("#toolbar_img_delall").click(function(e){
        $.ajax({
            url: `./api/file/remove`,
            type: 'get',
            data:{path:"assets/tools/capture",relative:true},
            async: false,
            success: function (res) {
                $("#imgs_con").empty();
                $("#imglist_size").text(0);
            },
            error: function (err) {
              alert('删除异常')
            }
          })
    });

    $("#toolbar_zoom_upload").click(function(e){
        // alert('1')
        uploadFile(uploadDir);
    });

    $(menus[getQueryString("type")]).click();

    
};


// window.onload = function (e) {
//     image.onload = function () {
//         $("#image_loading").hide();
//         image_data_object = getImageData();
//         $(conimg).scrollLeft(0)
//         $(conimg).scrollTop(0)

//         $('#header_pixels').text(`${image.width} x ${image.height}`)
//         $(".zoomWindow").css("background-size",`${image.width}px ${image.height}px`)
//         if (image.height > image.width) {
//             $(image).css("height","100%" );
//             $(image).css("width", "auto");
//         } else {
//             $(image).css("width", "100%");
//             $(image).css("height", "auto");
//         }

//         // zoom($(image), "window", "crosshair");

//         if($("#imgs_con").children().length<1){
//             getImgList();
//         }else{
//             //点了上传或者重新截图
//         }
        
//     }

//     showPicture();

//     $("#toolbar_img_capture").click(function(e){
//         $("#imgs_con").empty();
//         showPicture();
//     });

//     $("#toolbar_img_delall").click(function(e){
//         $.ajax({
//             url: `${baseUrl}/api/file/remove`,
//             type: 'get',
//             data:{path:"sdcard/airscript/screen/capture"},
//             async: false,
//             success: function (res) {
//                 $("#imgs_con").empty();
//                 $("#imglist_size").text(0);
//             },
//             error: function (err) {
//               alert('删除异常')
//             }
//           })
//     }); 

//     $("#toolbar_zoom_upload").click(function(e){
//         // alert('1')
//         uploadFile(uploadDir);
//     });
// };

function showPicture() {
    $("#image_loading").show();
    var picName = `${new Date().getTime()}.png`;
    image.src = baseUrl + `/api/tool/screen/capture?name=${picName}`
    $(image).attr("path",captureDir+picName);
    $(".zoomWindow").css("background-image",`url('${image.src}')`)
}

function showImg(url) {
    $("#image_loading").show();
    image.src = `./api/file/getpicture?path=${url}`;
    $(image).attr("path",url);
    $(".zoomWindow").css("background-image",`url('${image.src}')`)
}



function getImgList(cap){
    $("#imgs_con").empty();
    $("#imagelist_loading").show();
    $.ajax({
        url: `${api_tool_capture_list}?capture=${cap}`,
        type: 'get',
        contentType:'application/json',
        data:{},
        dataType:'json',
        async: true,
        success: function (res) {

            // imglist = res.data;
            $("#imagelist_loading").hide();

            $("#imglist_size").text(res.data.length);

            if(res.data.length>0){
                res.data.forEach((item,index,arr)=>{
                    if(index==0){
                        //获取列表后,给
                        showImg(item.path)
                    }else{}

                    $(`<img  i="${item.path}"  class="imglist_item shadow hover-shadow" title="${item.name}\n${item.lastModified_format}\n${item.length_format}" src="./api/file/getpicture?path=${item.path}&maxheight=${$("#imgs_con").height()}">`).appendTo("#imgs_con");
                });
                $(".imglist_item").eq(0).addClass("imglist_item_active");
                $(".imglist_item").eq(0).addClass("shadow-success-lg");
            }
            

            $(".imglist_item").mousemove(imagelist_mouseover);
            $(".imglist_item").click(function(e){
                clearmarks();
                scope_pos = [null, null];
                $("#image_loading").show();
                image.src = `./api/file/getpicture?path=${$(e.target).attr('i')}`
                $(image).attr('path',$(e.target).attr('i'));
                $(".zoomWindow").css("background-image",`url('${image.src}')`)
                $(".imglist_item").removeClass("imglist_item_active")
                $(".imglist_item").removeClass("shadow-success-lg")
                $(e.target).addClass("imglist_item_active")
                $(e.target).addClass("shadow-success-lg")
            });

            
        },
        error: function (err) {
          $("#imagelist_loading").hide();
          alert(err)
        }
      })
}

function getImageData() {
    $(image).css("height", "auto");
    $(image).css("width", "auto");
    var cvs = document.getElementById('preview_img_canvas');
    cvs.width = image.width;
    cvs.height = image.height;
    var ctx = cvs.getContext('2d');
    ctx.drawImage(image, 0, 0);
    return ctx.getImageData(0, 0, image.width, image.height);
}

//获取元素的纵坐标
function getTop(e) {
    var offset = e.offsetTop;
    if (e.offsetParent != null) offset += getTop(e.offsetParent);
    return offset;
}

//获取元素的横坐标
function getLeft(e) {
    var offset = e.offsetLeft;
    if (e.offsetParent != null) offset += getLeft(e.offsetParent);
    return offset;
}

//获取鼠标针对于父元素的位置
function mouseParentPos(e) {
    var x, y;
    return {
        x: e.clientX - conimg.offset().left+conimg.scrollLeft(),
        y: e.clientY - conimg.offset().top+conimg.scrollTop()
    };
};

//获取鼠标在页面中的位置
function mousePos() {
    var x, y;
    var e = window.event;
    return {
        x: e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft,
        y: e.clientY + document.body.scrollTop + document.documentElement.scrollTop
    };
};

//获取鼠标在图片上的位置及颜色（像素级）
function getPointOfImage() {
    //获取鼠标相对于整个页面的位置
    var pos = mousePos();
    var page_mouse_x = pos.x
    var page_mouse_y = pos.y;
    //获取图片元素的左上角的位置
    var img_x = getLeft(image);
    var img_y = getTop(image);
    //获取容器滚动条滚动的距离
    var distance_scroll_x = $("#container_img").scrollLeft();
    var distance_scroll_y = $("#container_img").scrollTop();
    //获取图片元素的宽度（实际的，而不仅是显示的）
    var img_width = image.offsetWidth;
    img_height = image.offsetHeight;
    //计算鼠标所在的图片上的位置距离左上角起始点的距离占宽高的百分比
    var percent_x = (page_mouse_x - img_x + distance_scroll_x) / img_width;
    var percent_y = (page_mouse_y - img_y + distance_scroll_y) / img_height;
    //获取图片的原始像素级坐标和颜色
    var pos_pixel_x = image_data_object.width * percent_x;
    var pos_pixel_y = image_data_object.height * percent_y;
    pos_pixel_x = Math.floor(pos_pixel_x);
    // pos_pixel_x = toInt(pos_pixel_x, 0.9);
    pos_pixel_y = Math.floor(pos_pixel_y);
    // pos_pixel_y = toInt(pos_pixel_y, 0.9);
    var index = (pos_pixel_x + 1 + (pos_pixel_y) * image_data_object.width - 1) * 4;
    var pos_pixel_color = {
        r: image_data_object.data[index],
        g: image_data_object.data[index + 1],
        b: image_data_object.data[index + 2],
        a: image_data_object.data[index + 3]
    };
    return { x: pos_pixel_x, y: pos_pixel_y, color: pos_pixel_color };
}

function showZoomCon(e){
    // alert($(image).position().left)
    // $(image).posation().x;
    // $(".zoomContainer").fadeIn(200,function(e){
    //     // $(".zoomWindow").show();
    // });

    $(".zoomContainer").show();

    var left = image.width+ $(image).position().left +$(conimg).position().left;
    var conwidth = $("#img_contain").width();
    var top = $("#img_contain").position().top;
    // alert(conwidth)
    if(left>conwidth){
        left = conwidth;
    }

    $(".zoomContainer").css('left',left);
    $(".zoomContainer").css('top',top);

    var zoomwindow = $(".zoomWindow");

    var leftoff = e.x-(zoomwindow.width()/2);
    leftoff = leftoff*-1;
    // alert(leftoff)
    var topoff = e.y-(zoomwindow.height()/2);
    topoff = topoff*-1;

    zoomwindow.css('background-position',`${leftoff}px ${topoff}px`);

}

function img_mousemove(e) {
    //处理显示鼠标坐标点图色信息的逻辑
    is_image_mouseover = true;
    $(".choose_colors_item_input").blur()
    
    var current_pos = getPointOfImage();
    showZoomCon(current_pos)
    pos_current = current_pos;
    info_XY.text("X：" + current_pos.x+" Y:"+current_pos.y);
    // info_Y.text("Y：" + current_pos.y);
    var r = current_pos.color.r.toString(16);
    var g = current_pos.color.g.toString(16);
    var b = current_pos.color.b.toString(16);
    r = r.length > 1 ? r : "0" + r;
    g = g.length > 1 ? g : "0" + g;
    b = b.length > 1 ? b : "0" + b;
    var rgb_str = r.toUpperCase() + g.toUpperCase() + b.toUpperCase();
    info_RGB.text("#" + rgb_str);
    info_color.css("background-color", "#" + rgb_str);

    mouse_move_xyc = {x:current_pos.x , y:current_pos.y,c:rgb_str};
 

    //处理拖动鼠标选择范围的逻辑
    if (!is_mouse_downed) { //如果鼠标不是按下状态，直接退出
        return false;
    }
    if (!is_show_box) {
        is_show_box = true;
    }
    var pos = mouseParentPos(e);
    var x_current = pos.x;
    var y_current = pos.y;
    var width = x_current - x_mouse_down;
    var height = y_current - y_mouse_down;
    part_box.css("width", width + "px");
    part_box.css("height", height + "px");
    if (width > 0 & height > 0) {
        part_box.css("display", "block");
        // p2.val(current_pos.x + "," + current_pos.y);
        // alert(1)
        if(findimage_capture){
            scope_pos_findimg[1] = current_pos;
        }else{
            scope_pos[1] = current_pos;
            p1.text(pos_mouse_down.x + "," + pos_mouse_down.y+","+current_pos.x + "," + current_pos.y);
        }
    }
    
    
    if(findimage_capture){
        scope_pos_findimg_path = $(image).attr("path");
        scope_pos_findimg[0] = pos_mouse_down;
    }else{
        scope_pos[0] = pos_mouse_down;
    }
    // generate_code();
    return false;
}

function img_onmouseout(e){
    // $(".zoomWindow").fadeOut(200,function(e){
        is_image_mouseover = false;   
    // });
    $(".zoomContainer").hide();
}

//图片上的鼠标按下事件
function img_mousedown(e) {
    // alert(conimg.scrollTop())

    scope_pos = [null, null];
    if(findimage_capture){
        scope_pos_findimg  = [null, null];
    }
    $("#header_rect").text("");
    is_mouse_downed = true;
    var pos = mouseParentPos(e);
    x_mouse_down = pos.x;
    y_mouse_down = pos.y;
    $(part_box).removeClass("shadow-dark-lg");
    part_box.css("left", x_mouse_down + "px");
    part_box.css("top", y_mouse_down + "px");
    part_box.css("width", "0px");
    part_box.css("height", "0px");
    part_box.css("display", "none");
    pos_mouse_down = getPointOfImage();
    is_show_box = false;
    return false;
}

function changeBoxRect(){
    // alert(conimg.scrollLeft())
    var boxp = part_box.position();
    var boxwidth = part_box.width();
    var boxheight = part_box.height();
    var maxWidth = conimg.width();
    var maxHeight = conimg.height();

    var relwidth = maxWidth/(boxwidth/image.width);
    var relHeight = relwidth/(image.width/image.height);
    var relBoxWidth = (boxwidth/image.width)* relwidth;
    var relBoxHight = (boxheight/image.height)*relHeight;
    if(relBoxHight>maxHeight){
         relHeight = maxHeight/(boxheight/image.height);
         relwidth = relHeight/(image.height/image.width);
         relBoxWidth = (boxwidth/image.width)* relwidth;
         relBoxHight = (boxheight/image.height)*relHeight;
    }



    var relBoxLeft = ((boxp.left+conimg.scrollLeft())/image.width)* relwidth;
    var relBoxTop = ((boxp.top+conimg.scrollTop())/image.height)*relHeight;

    
    
    if(boxwidth>0 && boxheight>0){
        // alert(relwidth+"?"+relHeight)
        $(image).css("width",relwidth+"px");
        $(image).css("height","auto");

        part_box.css("left", relBoxLeft + "px");
        part_box.css("top", relBoxTop + "px");
        part_box.css("width", relBoxWidth+"px");
        part_box.css("height", relBoxHight+"px");

        conimg.scrollLeft(relBoxLeft)
        conimg.scrollTop(relBoxTop)

        // $("#img_contain").scrollLeft(relBoxLeft)
        // $("#img_contain").scrollLeft(relBoxTop)

        // alert(maxwidth)
        // alert(1)
        

    }

    
    
}

//图片上鼠标抬起事件
function img_mouseup(e) {
    is_mouse_downed = false;
  
    // if (!testPosInScope()) {
    //     scope_pos = [null, null];
    //     p1.val("");
    //     p2.val("");
    //     part_box.css("display", "none");
    //     alert("所取色点不在所选范围之内，请重新取色点或重新选择范围！");
    // }
    

    if(findimage_capture){
        captureRect();//findimg
    }else{
        changeBoxRect();

        makeFindColorsStr();
    
        makeOcrStr();
    
        changeImageMarkSize();

        makeFindImageStr();
    }

    findimage_capture = false;
    $("#findimage_capture").hide();
    
    return false;
}

$("#img_preview").mouseup(img_mouseup);
$("#img_preview").mousedown(img_mousedown);
$("#img_preview").mousemove(img_mousemove);
$("#img_preview").mouseout(img_onmouseout);


function imagelist_mouseover(e){
    $("#delect_img").show();
    // alert($(e.target).attr('src'))
    var dom = $(e.target);
    img_deleft_dom = $(e.target);
    var left = dom.width()+ dom.position().left- dom.scrollLeft() - $("#delect_img").width()-10;
    // alert(left)
    $("#delect_img").css("left",left+"px");
}

// function imagelist_mouseout(e){
//     $("#delect_img").hide();
// }
 


// $(".imglist_item").mouseout(imagelist_mouseout);
$("#delect_img").click(function(e){
    // alert(1)
    img_deleft_dom.remove();
    $("#delect_img").hide();

    $.ajax({
        url: `./api/file/remove`,
        type: 'get',
        data:{path:$(img_deleft_dom).attr('i')},
        async: false,
        success: function (res) {
            $("#imglist_size").text($("#imgs_con").children().length);
            // alert('12')
        },
        error: function (err) {
          alert('删除异常')
        }
      })

    // $(img_deleft_dom).animate({ width: 0 }, 400);
});


$("#toolbar_zoom_reset").click(function(e){

    // scope_pos = [null, null];

    if (image.height > image.width) {
        $(image).css("height","100%" );
        $(image).css("width", "auto");
    } else {
        $(image).css("width", "100%");
        $(image).css("height", "auto");
    }

    $(conimg).scrollLeft(0)
    $(conimg).scrollTop(0)

    // part_box.css("left", "0px");
    // part_box.css("top", "0px");
    // part_box.css("width", "0px");
    // part_box.css("height", "0px");
    // part_box.css("display", "none");

    changeImageMarkSize();

});

$("#toolbar_zoom_in").click(function(e){
    $(image).css("height",image.height*1.1);
    $(image).css("width", "auto");
    changeImageMarkSize();
    e.stopPropagation(); //阻止传递事件
});

$("#toolbar_zoom_out").click(function(e){
    $(image).css("height",image.height*0.9);
    $(image).css("width", "auto");
    changeImageMarkSize();
    e.stopPropagation(); //阻止传递事件
});


function uploadFile(p) {
    $("#fileupload").trigger('click');
    $("#fileupload").change(function (e) {
        // alert($('#fileupload')[0].files.length)
        if ($('#fileupload')[0].files.length >= 1) {
            var formData = new FormData();
            var fName = $('#fileupload')[0].files[0].name;
            // var fName = new Date().getTime()+".png"
            formData.append("data", e.target.files[0]);
            // formData.append("path", uploadDir+fName);
            $.ajax({
                url: baseUrl+'/api/file/upload?path='+(uploadDir+fName),
                type: 'POST',
                cache: false,
                data: formData,
                processData: false,
                contentType: false
            }).done(function (res) {
                // $("#upload_pic").text("导入图片");
                // addPicCacheListItem(fName,false)
                getImgList(false)
                
            }).fail(function (res) {
                // getFilesList();
                // $("#upload_pic").text("导入图片");
                alert("上传失败")
            });
        }else{
            $("#upload_pic").text("导入图片");
        }

    });
}

function getQueryString(name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return unescape(r[2]);
    }
    return null;
}

function copy2(copyTxt) {
    var createInput = document.createElement("input");
    createInput.value = copyTxt;
    document.getElementById("nodetree_refresh").appendChild(createInput);
    createInput.select();
    document.execCommand("Copy");
    createInput.className = 'createInput';
    createInput.style.display = "none";
  }