var findimage_itemdom = $(".findimg_item_dom");
var findimageMarks = null;

var findimage_capture = false;
var scope_pos_findimg = [null, null];
var scope_pos_findimg_path = "";
var findtips={
    find:"find:找到一个结果",
    find_all:"finds:找到所有满足条件的结果",
    find_all:"find_all:先使用find_all_template匹配,找不到后使用all_sift算法匹配",
    find_sift:"find_sift:找到一个最相似的图,支持全分辨率,速度慢",
    find_all_sift:"find_all_sift:找到所有相似图,支持全分辨率,速度慢",
    find_template:"find_template:模版匹配一个最相似的结果,不支持全分辨率,速度快.",
    find_all_template:"find_all_template:模版匹配所有结果,不支持全分辨率,速度快."
}
var findImageDao ={}


$(document).ready(function () {
    loadModels();

    $("#findimg_save").click(function(e){
        var savePath = $("#findimg_modules").find("option:selected").attr('path');
        var picname= $("#input_findimage_name").val();
        if(picname.length<1){
            alert('缺少图片名称')
            return;
        }

        if(scope_pos_findimg[0]==null || scope_pos_findimg[1]==null){
            alert('(缺少保存区域) 请先点击截图括选区域')
            return;
        }

        savePath = `${savePath}/res/img/${picname}.png`


        savecaptureRect(savePath,false)
    })

    $("#findimg_capture").click(function(e){
        // alert('12')
        findimage_capture = true;
        $("#findimage_capture").show();
    });

    $("#findimage_capture").click(function(e){
        findimage_capture = false;
        $("#findimage_capture").hide();
    });

    $("#findimage_test_run").click(function(e){
        // alert("1")
        testfindImage();
    })

    $("#findimg_methods").change(function(e) {    
        makeFindImageStr();
    });




});

function makeFindImageStr(){
    findImageDao = {}
    var method = $("#findimg_methods").find("option:selected").text();
    $("#find_method_des").text(findtips[method])

    var imagename = $("#input_findimage_name").val();


    var rectStr = "";
    if(scope_pos[0]!=null && scope_pos[1]!=null){
            findImageDao.rect = {left:scope_pos[0].x,top:scope_pos[0].y,right:scope_pos[1].x,bottom:scope_pos[1].y};
            rectStr = `,rect=[${scope_pos[0].x},${scope_pos[0].y},${scope_pos[1].x},${scope_pos[1].y}]`
    }

    var conf = "";

    if($("#input_findimage_confidence").val().length>0){
        conf = `.confidence(${$("#input_findimage_confidence").val()})`
    }

    document.getElementById("findimage_code_input").value = `FindImages('${imagename}.png' ${rectStr}${conf}).${method}()`
    
}


function loadModels() {

    $.ajax({
            url: model_list,
            type:'POST',
            contentType:'application/json',
            dataType:'json',
            async: true,
            success: function (res) {
                $("#models").empty();

                if(res.data.length<1){
                    $("#model_create").click();
                    return;
                }

                res.data.forEach(function (e) {
                    var item = $(`<option value="1" path="${e.path}" >${e.name}</option>`);
                    $("#findimg_modules").append(item);

                });

            },
            error: function (err) {
                $("#findcolor_test_loading").hide();
              alert(err)
            }
          })
}


function captureRect() {
    // if(scope_pos==null)
    if($("#con_findimage").is(":visible")){
        var rect = {left:scope_pos_findimg[0].x,top:scope_pos_findimg[0].y,right:scope_pos_findimg[1].x,bottom:scope_pos_findimg[1].y}
        // var path = $(image).attr("path");
        var findpartsrc = `/api/file/getpicture?path=${scope_pos_findimg_path}&rect=${JSON.stringify(rect)}`;
        document.getElementById('findimg_partimg').src = findpartsrc;
    }else{
        
    }
    
}

function savecaptureRect(savepath,ysave) {
    // if(scope_pos==null)
    if($("#con_findimage").is(":visible")){
        var rect = {left:scope_pos_findimg[0].x,top:scope_pos_findimg[0].y,right:scope_pos_findimg[1].x,bottom:scope_pos_findimg[1].y}
        var path = scope_pos_findimg_path;
        var findpartsrc = `/api/file/getpicture?path=${path}&rect=${JSON.stringify(rect)}&save=${savepath}&ysave=${ysave}`;
        // document.getElementById('findimg_partimg').src = findpartsrc;
        $.ajax({
            url: findpartsrc,
            type: 'get',
            data:{},
            async: false,
            success: function (res) {
                if(res.includes('-1')){
                    res = JSON.parse(res)
                        if(confirm(res.msg+",是否覆盖?")){
                            savecaptureRect(savepath,true)
                        }else{

                        }
                }

                // alert("存储成功")
            },
            error: function (err) {
            //   $("#ocr_test_loading").hide();
              alert(err.msg)
            }
          })

    }else{
        
    }
    
}


function testfindImage(){

    var method = $("#findimg_methods").find("option:selected").text();

    findImageDao.image = screenTempDir+"findimage_test.png";
    findImageDao.screen = $(image).attr("path");
    var conStr = $("#input_findimage_confidence").val();
    if(conStr.length>0){
        findImageDao.sim = parseFloat(conStr);
    }else{
        findImageDao.sim = 0;
    }

    $("#findimage_reslist").empty();

    $("#findimage_test_loading").show();

    findImageDao.findtype = method

    savecaptureRect(findImageDao.image,true)

    $.ajax({
            url: fun_findimages,
            type:'POST',
            contentType:'application/json',
            dataType:'json',
            data:JSON.stringify(findImageDao),
            async: true,
            success: function (res) {
                $("#findcolor_test_loading").hide();
                $("#findimage_test_loading").hide();
                $("#findcolor_res_reset").show();
                $("#findcolor_res").text(res.data.length)
                $("#findcolor_res").show();
                $("#findimage_reslist").empty();
                $("#findimage_res").empty();

                findimageMarks = res.data;

                res.data.forEach((item,index,arr)=>{

                    //--
                    var idom = ocrres_itemdom.clone(true);
                        idom.find(".ocr_item_dom_text").text(item.result[0]+","+item.result[1])
                        var conf = item.confidence+"";
                        idom.find(".conf").text(conf.substring(0,4));
                        idom.find(".rect").text(`${item.rectangle[0][0]},${item.rectangle[0][1]},${item.rectangle[3][1]},${item.rectangle[3][1]}`);
                        $(idom).addClass("ocr_item_dom"+index);
                        $(idom).appendTo("#findimage_reslist");

                        $(idom).on('mouseover', function() {
                            $(idom).addClass("list-group-item-success");
                            $(`.ocr_marks${index}`).addClass("ocr_markshover")
                            $(`.ocr_marks${index}`).addClass("shadow-dark-lg")

                        });

                        $(idom).on('mouseout', function() {
                            $(idom).removeClass("list-group-item-success");
                            $(`.ocr_marks${index}`).removeClass("ocr_markshover")
                            $(`.ocr_marks${index}`).removeClass("shadow-dark-lg")
                        });

                        $(idom).click(function(e){
                            // makeOcrStr()
                        });

                        idom.find(".ocr_item_dom_text").click(function(e){
                            // $("#input_ocr_mathcer").val(idom.find(".ocr_item_dom_text").text());
                        });

                        idom.find(".rect").click(function(e){
                            // --更改识别范围
                            // var p_left= item.region_position.left -5;
                            // var p_top= item.region_position.top -5;
                            // var p_right= item.region_position.right +5;
                            // var p_bottom= item.region_position.bottom +5;

                            // scope_pos[0] = {
                            //     x:p_left,
                            //     y:p_top
                            // }

                            // scope_pos[1] = {
                            //     x:p_right,
                            //     y:p_bottom
                            // }

                            // $(part_box).show();

                            // changeImageMarkSize();

                            // changeBoxRect();
                        })

                        idom.find(".conf").click(function(e){
                            // -- 更改识别可信度
                            // $("#input_ocr_similar").val(conf.substring(0,4))

                        })

                        // add mark
                        var markDom =  $(`<div class="ocr_marks${index} ocr_marks"></div>`);
                        markDom.appendTo("#findimage_res")

                        // $(markDom).click(function(e){
                        //     $("#input_ocr_mathcer").val($(`.ocr_item_dom${index}`).find(".ocr_item_dom_text").text());
                        //     makeOcrStr()
                        // });

                        $(markDom).on('mouseover', function() {
                            $(`.ocr_item_dom${index}`).addClass("list-group-item-success");
                            $(markDom).addClass("ocr_markshover")
                            $(markDom).addClass("shadow-dark-lg")
                            let top = $(`.ocr_item_dom${index}`).offset().top - $(`#findimage_res_con`).offset().top;
                            top = $(`#findimage_reslist`).scrollTop()+top;
                            // let pt =  $(`.ocr_item_dom${index}`).posation().top
                            $(`#findimage_reslist`).scrollTop(top);
                        });

                        $(markDom).on('mouseout', function() {
                            $(`.ocr_item_dom${index}`).removeClass("list-group-item-success");
                            $(markDom).removeClass("ocr_markshover")
                            $(markDom).removeClass("shadow-dark-lg")
                        });

                        changeImageMarkSize();

                    // idom.find(".rect").text(item.region_position.left+","+item.region_position.top+","+item.region_position.right+","+item.region_position.bottom);
                });
            },
            error: function (err) {
                $("#ocr_test_loading").hide();
                alert(err)
            }
    })

    // $.ajax({
    //     url: `${fun_findimages}?method=${method}`,
    //     type: 'get',
    //     data:{findImage:JSON.stringify(findImageDao)},
    //     async: true,
    //     success: function (res) {
    //         $("#findimage_test_loading").hide();
    //             $("#findcolor_res_reset").show();
    //             $("#findcolor_res").text(res.data.length)
    //             $("#findcolor_res").show();
    //             $("#findimage_reslist").empty();
    //             $("#findimage_res").empty();
    //
    //         findimageMarks = res.data;
    //
    //         res.data.forEach((item,index,arr)=>{
    //
    //             //--
    //             var idom = ocrres_itemdom.clone(true);
    //                 idom.find(".ocr_item_dom_text").text(item.result.x+","+item.result.y)
    //                 var conf = item.confidence+"";
    //                 idom.find(".conf").text(conf.substring(0,4));
    //                 idom.find(".rect").text(`${item.rectangle[0].x},${item.rectangle[0].y},${item.rectangle[3].x},${item.rectangle[3].y}`);
    //                 $(idom).addClass("ocr_item_dom"+index);
    //                 $(idom).appendTo("#findimage_reslist");
    //
    //                 $(idom).on('mouseover', function() {
    //                     $(idom).addClass("list-group-item-success");
    //                     $(`.ocr_marks${index}`).addClass("ocr_markshover")
    //                     $(`.ocr_marks${index}`).addClass("shadow-dark-lg")
    //
    //                 });
    //
    //                 $(idom).on('mouseout', function() {
    //                     $(idom).removeClass("list-group-item-success");
    //                     $(`.ocr_marks${index}`).removeClass("ocr_markshover")
    //                     $(`.ocr_marks${index}`).removeClass("shadow-dark-lg")
    //                 });
    //
    //                 $(idom).click(function(e){
    //                     // makeOcrStr()
    //                 });
    //
    //                 idom.find(".ocr_item_dom_text").click(function(e){
    //                     // $("#input_ocr_mathcer").val(idom.find(".ocr_item_dom_text").text());
    //                 });
    //
    //                 idom.find(".rect").click(function(e){
    //                     // --更改识别范围
    //                     // var p_left= item.region_position.left -5;
    //                     // var p_top= item.region_position.top -5;
    //                     // var p_right= item.region_position.right +5;
    //                     // var p_bottom= item.region_position.bottom +5;
    //
    //                     // scope_pos[0] = {
    //                     //     x:p_left,
    //                     //     y:p_top
    //                     // }
    //
    //                     // scope_pos[1] = {
    //                     //     x:p_right,
    //                     //     y:p_bottom
    //                     // }
    //
    //                     // $(part_box).show();
    //
    //                     // changeImageMarkSize();
    //
    //                     // changeBoxRect();
    //                 })
    //
    //                 idom.find(".conf").click(function(e){
    //                     // -- 更改识别可信度
    //                     // $("#input_ocr_similar").val(conf.substring(0,4))
    //
    //                 })
    //
    //                 // add mark
    //                 var markDom =  $(`<div class="ocr_marks${index} ocr_marks"></div>`);
    //                 markDom.appendTo("#findimage_res")
    //
    //                 // $(markDom).click(function(e){
    //                 //     $("#input_ocr_mathcer").val($(`.ocr_item_dom${index}`).find(".ocr_item_dom_text").text());
    //                 //     makeOcrStr()
    //                 // });
    //
    //                 $(markDom).on('mouseover', function() {
    //                     $(`.ocr_item_dom${index}`).addClass("list-group-item-success");
    //                     $(markDom).addClass("ocr_markshover")
    //                     $(markDom).addClass("shadow-dark-lg")
    //                     let top = $(`.ocr_item_dom${index}`).offset().top - $(`#findimage_res_con`).offset().top;
    //                     top = $(`#findimage_reslist`).scrollTop()+top;
    //                     // let pt =  $(`.ocr_item_dom${index}`).posation().top
    //                     $(`#findimage_reslist`).scrollTop(top);
    //                 });
    //
    //                 $(markDom).on('mouseout', function() {
    //                     $(`.ocr_item_dom${index}`).removeClass("list-group-item-success");
    //                     $(markDom).removeClass("ocr_markshover")
    //                     $(markDom).removeClass("shadow-dark-lg")
    //                 });
    //
    //                 changeImageMarkSize();
    //
    //             // idom.find(".rect").text(item.region_position.left+","+item.region_position.top+","+item.region_position.right+","+item.region_position.bottom);
    //         });
    //
    //     },
    //     error: function (err) {
    //       $("#ocr_test_loading").hide();
    //       alert(err)
    //     }
    //   })

}
