// var baseUrl = "http://192.168.31.58:9096";

var itemdom = $(".choose_colors_item");
var markdom = $(".findcolor_marks");
var simColorInput = ("#input_color_sim");
var oriColorInput = ("#input_color_ori");
var spaceColorInput = ("#input_color_space");
var chooseColors = new Array(10);
var findColorMarks = null;
var findColor ={
    rect:null,
    colors:"",
    ore:2,
    colorDiff:"#050505"


};
var compareColors = {
    colors:"",
    colorDiff:"#050505"
};

var findcolor_type = 0;
var ocr_type = 0;


$(document).ready(function () { // 初始化
    $("#findColor_res").empty();
    //增加颜色框
    addColorItem()

    //复制逻辑
    $("#findColor_copy").click(function(e){
        copy($("#findcolors_input").val());
    });

    // $("#findColor_test").click(function(e){
    //     copy($("#findcolors_input").val());
    // });

    $("#findColor_test").click(function(e){
        if(findColor.colors.length<1){
            alert('缺少颜色特征')
            return;
        }

        $("#findcolor_test_loading").show();

        clearmarks();

        // alert(JSON.stringify(findColor))

        let tempfind = JSON.parse(JSON.stringify(findColor))
        tempfind.file = $(image).attr("path")

        // alert(JSON.stringify(tempfind))

        $.ajax({
            url: fun_findcolors,
            type:'POST',
            contentType:'application/json',
            dataType:'json',
            data:JSON.stringify(tempfind),
            async: true,
            success: function (res) {
                $("#findcolor_test_loading").hide();
                $("#findcolor_res_reset").show();
                $("#findcolor_res").show();
                $("#findresult").empty();
                $("#findColorres_count").text(res.data.length)
                findColorMarks = res.data;
                $("#findcolor_res").text(res.data.length)
                res.data.forEach((item,index,arr)=>{
                    var idom = markdom.clone(true);
                    idom.find(".mark_xy").text(`(${item.x},${item.y})`)
                    idom.find(".marknumber").text(index+1);
                    $(idom).appendTo("#findColor_res");
                });
                // $('.findres').modal('show')
                changeImageMarkSize();
            },
            error: function (err) {
                $("#findcolor_test_loading").hide();
              alert(err)
            }
          })
    });

    $("#compareColor_test").click(function(e){
        if(compareColors.colors.length<1){
            alert('缺少颜色特征')
            return;
        }

        compareColors.path = $(image).attr("path")

        $.ajax({
            url: fun_comparecolors,
            type:'POST',
            contentType:'application/json',
            dataType:'json',
            data:JSON.stringify(compareColors),
            async: false,
            success: function (res) {
                alert(res.data);
            },
            error: function (err) {
              alert(err)
            }
          })
    });

    $("input").bind('input propertychange change',function(){
        makeFindColorsStr()
        makeOcrStr()
        makeFindImageStr()
    })

    $(".colorboard_nav").click(function(e){
        // alert($(e.target).html())
        // $(".active").removeClass("active");
        // $(e.target).find(".colorboard_nav").addClass("active");
        $(".colorboard_nav").removeClass("active");
        $(e.target).addClass("active");
       
        // alert($(e.target).html())
    });

    $("#toolbar_color_reset").click(function(e){
        $("#colors_con input").val("");
        $(".choose_colors_item_bgcolor").css("background-color","transparent")
        chooseColors = new Array(10);
        makeFindColorsStr()
    });

    $("#findcolor_res_reset").click(function(e){
        clearmarks();
    });

    $("#btn_findcolor").click(function(e){
        $("#con_findcolor_comaprecolor").show()
        $("#con_ocr").hide();
        $("#findcolor_body").show();
        $("#con_findimage").hide();
        $("#compare_body").hide();
    })

    $("#btn_comparecolor").click(function(e){
        $("#con_findcolor_comaprecolor").show()
        $("#con_ocr").hide();
        $("#con_findimage").hide();
        $("#compare_body").show();
        $("#findcolor_body").hide()
    })

    $("#btn_ocr").click(function(e){
        $("#con_ocr").show();
        $("#con_findcolor_comaprecolor").hide()
        $("#con_findimage").hide();
    })

    $("#btn_findimage").click(function(e){
        $("#con_findimage").show();
        $("#con_findcolor_comaprecolor").hide()
        $("#con_ocr").hide();
    })

    $("#btn_findcolor").trigger('click');



    
    //-- copy logic
    $("#findColor_copy").click(function(e){
        copy2($("#findcolors_input").text())
    });

    $("#compareColor_copy").click(function(e){
        var str = $("#compareColor_input").val();
        copy2(str)
    });

    $("#ocr_copy").click(function(e){
        copy2($("#ocrc_ode_input").val())
    });

    $("#findimg_copy").click(function(e){
        copy2($("#findimage_code_input").val())
    });

    // -- findcolor type
    $("#p_findcolor_one").click(function(){
        // alert(document.getElementById("p_i_code").value)
        findcolor_type = "find"
        $("#findcolor_type_des").text("查找一个")
        makeFindColorsStr();
    })

    $("#p_findcolor_all").click(function(){
        // alert(document.getElementById("p_i_code").value)
        $("#findcolor_type_des").text("查找全部")
        findcolor_type = "find_all"
        makeFindColorsStr();
    })

    $("#p_ocr_one").click(function(){
        // alert(document.getElementById("p_i_code").value)
        ocr_type = "find"
        $("#ocr_type_des").text("查找一个")
        makeOcrStr();
    })

    $("#p_ocr_all").click(function(){
        // alert(document.getElementById("p_i_code").value)
        $("#ocr_type_des").text("查找全部")
        ocr_type = "find_all"
        makeOcrStr();
    })

    $(oriColorInput).on('change', function () {
       makeFindColorsStr()
    })
    

});

$(document).keypress(function(e){
    var keynumber = e.keyCode-48;
    if(keynumber>0 && keynumber<10 && is_image_mouseover){
        
        var cdom = $("#choose_colors_item_"+keynumber);
        cdom.find(".choose_colors_item_input").val(mouse_move_xyc.x+","+mouse_move_xyc.y+" #"+mouse_move_xyc.c)
        cdom.find(".choose_colors_item_bgcolor").css("background-color","#"+mouse_move_xyc.c)
        chooseColors[keynumber] = mouse_move_xyc;
        makeFindColorsStr();
        
        // var bgitemdom = cdom.find(".choose_colors_item_bgcolor")
        
    }
    
    // print(cdom.val())
});

function makeFindColorsStr(){
    findColor = {};
    var rectStr = "";
    var colorsStr = "";
    var sim="";
    var ori = "";
    var space ="";

    let find_strs = []

    //-颜色
    chooseColors.forEach(function(k){
        if(k!=null){
            if(colorsStr.length>0){
                colorsStr = colorsStr+'|'
            }
            colorsStr = colorsStr+`${k.x},${k.y},#${k.c}`;
        }
    });

    findColor.colors = colorsStr;
    compareColors.colors = colorsStr;
    colorsStr = '\''+colorsStr+'\'';
    find_strs.push(colorsStr)

    //-rect
    if(scope_pos[0]!=null && scope_pos[1]!=null){
        find_strs.push(`rect=[${scope_pos[0].x},${scope_pos[0].y},${scope_pos[1].x},${scope_pos[1].y}]`)
        findColor.rect =[scope_pos[0].x,scope_pos[0].y,scope_pos[1].x,scope_pos[1].y];
    }





    if($(simColorInput).val()!="0.9"){
        sim = `sim= ${$(simColorInput).val()}`
        find_strs.push(sim)
        findColor.sim = $(simColorInput).val();
    }


    if($(oriColorInput).val()!="2"){
        ori = `ore=${$(oriColorInput).val()}`
        find_strs.push(ori)
        findColor.ore = $(oriColorInput).val();
    }

    if($(spaceColorInput).val()!="5"){
        space = `space=${$(spaceColorInput).val()}`
        find_strs.push(space)
        findColor.space = $(spaceColorInput).val();
    }

    var final_params = ""

    for (let i = 0; i < find_strs.length; i++) {
        if(i==0){
            final_params = find_strs[i];
        }else{
            final_params = final_params +"," +find_strs[i]
        }
    }

    var findtype= ".find()"
    findColor.res_num = "1";
    if(findcolor_type=="find_all"){
        findtype = ".find_all()"
        findColor.res_num = "-1";
    }

    // $("#findcolors_input").value("123")
    document.getElementById("findcolors_input").value = `FindColors(${final_params})${findtype}`;



    var diff_comparecolors = "";
    
    if($("#input_color_compare_diff").val()!="0.9"){
        diff_comparecolors = `,sim= ${$(simColorInput).val()}`
        compareColors.sim = $(simColorInput).val();
    }

    document.getElementById("compareColor_input").value = `CompareColors(${colorsStr}${diff_comparecolors}).compare()`;

    
}


function addColorItem(){
    // alert(1)
    $("#colors_con").children().remove();
    for (var i=1;i<10;i++)
    { 
        var newdom = itemdom.clone(true)
        newdom.find(".choose_colors_item_no").text(i);
        newdom.attr("id","choose_colors_item_"+i);

        newdom.find("input").attr("id","choose_colors_item_input_"+i);

        var dbtn =newdom.find("button");
        dbtn.attr("pos",i);

        dbtn.click(i,function(e){
            $("#choose_colors_item_input_"+e.data).val('');
            $("#choose_colors_item_"+e.data).find(".choose_colors_item_bgcolor").css("background-color","transparent")
            chooseColors[Number(e.data)] = null;
            makeFindColorsStr();
        });

        $(newdom).appendTo("#colors_con");
    }
}

function copy(str){
    const input = document.createElement('input') // 创建input对象
        // const testDiv = document.querySelector('#') // 获取需要复制文字的容器
        input.value = str// 设置复制内容
        document.body.appendChild(input) // 添加临时实例
        input.select() // 选择实例内容
        document.execCommand('Copy') // 执行复制
        document.body.removeChild(input) // 删除临时实例
}

function changeImageMarkSize(){
    
    var rimgw = image_data_object.width;
    var rimgh = image_data_object.height;

    var cimgw = image.width;
    var cimgh = image.height;

    //---change box
    if(scope_pos[0]!=null && scope_pos[1]!=null){
        var rboxw = scope_pos[1].x - scope_pos[0].x;
        var rboxh = scope_pos[1].y - scope_pos[0].y;
        //计算目标box 的 宽度和高度
        var tboxw = rboxw/(rimgw/cimgw);
        var tboxh = rboxh/(rimgh/cimgh);
        //计算目标box 的 left 和top值
        var tboxleft = scope_pos[0].x/(rimgw/cimgw);
        var tboxtop = scope_pos[0].y/(rimgw/cimgw);

        part_box.css("left", tboxleft + "px");
        part_box.css("top", tboxtop + "px");
        part_box.css("width", tboxw+"px");
        part_box.css("height", tboxh+"px");

        if (tboxw > 0 & tboxh > 0) {
            part_box.css("display", "block");
            $(part_box).addClass("shadow-dark-lg");
        }
    }
    


    //---change mark
    if(findColorMarks!=null){
        // alert('1 - enter')
        findColorMarks.forEach((item,index,arr)=>{
            var p =  findColorMarks[index];
            var markx = p.x/(rimgw/cimgw);
            var marky = p.y/(rimgw/cimgw);
            $('#findColor_res').children().eq(index).css({'left':markx+"px",'top':marky+"px"});
        });
    }


    if(ocrMarks!=null){
        // alert('1 - enter')
        ocrMarks.forEach((item,index,arr)=>{
            var p =  ocrMarks[index];
            var width = p.region_position[2][0] - p.region_position[0][0];
            var height = p.region_position[2][1] - p.region_position[0][1];
            var marky = p.region_position[0][1]/(rimgw/cimgw);
            var markx = p.region_position[0][0]/(rimgw/cimgw);
            var markw = width/(rimgw/cimgw);
            var markh = height/(rimgw/cimgw);
            $('#ocr_res').children().eq(index).css({'left':markx+"px",'top':marky+"px","width":markw+"px","height":markh+"px"});
        });
    }

    if(findimageMarks!=null){
        // alert('1 - enter')
        findimageMarks.forEach((item,index,arr)=>{
            var p =  findimageMarks[index];
            var width = p.rectangle[2][0] - p.rectangle[0][0];
            var height = p.rectangle[1][1] - p.rectangle[0][1];
            var marky = p.rectangle[0][1]/(rimgw/cimgw);
            var markx = p.rectangle[0][0]/(rimgw/cimgw);
            var markw = width/(rimgw/cimgw);
            var markh = height/(rimgw/cimgw);
            $('#findimage_res').children().eq(index).css({'left':markx+"px",'top':marky+"px","width":markw+"px","height":markh+"px"});
        });
    }
}

function clearmarks(){
    
    findColorMarks = null;
        $("#findColor_res").empty();
        $("#ocr_res").empty();
        $("#findimage_res").empty();
        $("#findcolor_res_reset").hide();
        $("#findcolor_res").hide();

    ocrMarks = null;
        $("#ocr_reslist").empty();
        $("#ocr_res").empty();
}




