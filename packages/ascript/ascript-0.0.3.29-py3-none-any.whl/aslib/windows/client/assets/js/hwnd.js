
var form;
var tree;

var nodeIdCount;
var selecor = {};
$(document).ready(function () {

    selecor = {};
    selecor.sels = [];
    selecor.model = Number($("#sel_model").val())
    selecor.find = -1;

    getwindows();



    $("#title_search").click(function (){
        filterwindows()
    })

    $("#sel_model").change(function () {
        selecor.model = Number($(this).val())
        makeSelectorCode();
        getwindows();
    })

    $("#sel_title_regx_add").click(function (data) {
            var value = $("#sel_title_regx").val().trim();
            if(value.length>0){
                selecor.sels.push({key:"title",value:[value]})
                makeSelectorCode()
            }
    })

    $("#sel_name_regx_add").click(function (data) {
            var value = $("#sel_name_regx").val().trim();
            if(value.length>0){
                selecor.sels.push({key:"name",value:[value]})
                makeSelectorCode()
            }
    })

        $("#sel_hwnd_regx_add").click(function (data) {
            var value = $("#sel_hwnd_regx").val().trim();
            if(value.length>0){
                selecor.sels.push({key:"hwnd",value:[Number(value)]})
                makeSelectorCode()
            }
        })

        $("#find_all").click(function (data) {
            selecor.find = -1;
            makeSelectorCode()
            getwindows();
        })

        $("#find_one").click(function (data) {
            selecor.find = 1;
            makeSelectorCode()
            getwindows();
        })

        $("#sel_reset").click(function (data) {
            selecor.sels = [];
            $("#sel_title_regx").val("")
            $("#sel_name_regx").val("")
            $("#sel_hwnd_regx").val("")
            makeSelectorCode();
        })

    // layui.use(function (){
    //     form = layui.form;
    //     tree = layui.tree;
    //
    //     // alert('1')
    //     form.on('checkbox(seltitle)',function (data){
    //         filterwindows();
    //     });
    //
    //
    //     layui.code({
    //         elem:"#code_pre",
    //         code:"Selector..."
    //     })
    //
    //     $("#sel_title_regx_add").click(function (data) {
    //         var value = $("#sel_title_regx").val().trim();
    //         if(value.length>0){
    //             selecor.sels.push({key:"title",value:[value]})
    //             makeSelectorCode()
    //         }
    //     })
    //
    //     $("#sel_name_regx_add").click(function (data) {
    //         var value = $("#sel_name_regx").val().trim();
    //         if(value.length>0){
    //             selecor.sels.push({key:"name",value:[value]})
    //             makeSelectorCode()
    //         }
    //     })
    //
    //     $("#sel_hwnd_regx_add").click(function (data) {
    //         var value = $("#sel_hwnd_regx").val().trim();
    //         if(value.length>0){
    //             selecor.sels.push({key:"hwnd",value:[Number(value)]})
    //             makeSelectorCode()
    //         }
    //     })
    //
    //     $("#find_all").click(function (data) {
    //         selecor.find = -1;
    //         makeSelectorCode()
    //         getwindows();
    //     })
    //
    //     $("#find_one").click(function (data) {
    //         selecor.find = 1;
    //         makeSelectorCode()
    //         getwindows();
    //     })
    //
    //     $("#sel_reset").click(function (data) {
    //         selecor.sels = [];
    //         $("#sel_title_regx").val("")
    //         $("#sel_name_regx").val("")
    //         $("#sel_hwnd_regx").val("")
    //         makeSelectorCode();
    //     })
    //
    // })

});

function makeSelectorCode() {
    var model_str = ""
    if(selecor.model===-1){
        model_str = selecor.model+"";
    }

    var sels_str = "";

    selecor.sels.forEach(function (item) {
        // alert(JSON.stringify(item))
        var item_value = item.value[0];

        if(typeof item_value ==="string"){
            item_value = '"'+item_value+'"'
        }

        sels_str = sels_str + "."+item.key+"("+item_value+")"
    })


    var find_str = ".find()";

    if(selecor.find ===-1){
        find_str = ".find_all()";
    }else if(selecor.find>1){
        find_str = ".find_all("+selecor.find+")";
    }

    // $("#code_pre").val("Selector("+model_str+")"+sels_str)

    // layui.code({
    //         elem:"#code_pre",
    //         theme:'dark',
    //         code:"Selector("+model_str+")"+sels_str+find_str
    // })

    $("#code_pre").text("Selector("+model_str+")"+sels_str+find_str)

}


var nodes = [];

function getwindows(){

    $.ajax({
        url:hwnd_windows,
        type:'POST',
        contentType:'application/json',
        dataType:'json',
        data:JSON.stringify(selecor),
        error:function (xhr,status,error) {

        },
        success:function (nodes) {
            nodeIdCount = 1;
            var zTreeObj;
            var setting = {
                view: {
                  addDiyDom: addDiyDom,  //自定义
                },
                data: {
                  key: {
                    children: 'children',
                    name: 'name'
                  }
                }
            };

            zNodes = nodes;
            // alert(1)
            zNodes = formatZnodes(zNodes)

            $(document).ready(function () {
                zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);
                zTreeObj.expandAll(true);
            });

            // filterwindows();
        }
    })
}

function formatZnodes(list) {
  function deleteEmptyArray(children) {
    children.forEach(item => {
      item.nodeId = nodeIdCount
      nodeIdCount++
      if (item.children.length === 0) {
        delete item.children
      } else {
        formatZnodes(item.children)
      }
    })
  }
  deleteEmptyArray(list)
  return list
}



function addDiyDom(treeId, treeNode) {
  var spantxt = $("#" + treeNode.tId + "_span").html();

  if (treeNode.clickable) {
    var clickDom = document.createElement("div");
    clickDom.innerHTML = spantxt
    clickDom.classList.add("click-btn")
    clickDom.classList.add("bg-gradient-success")
    clickDom.id = 'treenode_' + treeNode.nodeId
    // clickDom.onclick = function () {
    //   handleNodeDialog(treeNode)
    //   event.stopPropagation();
    // }
    $("#" + treeNode.tId + "_span").html(clickDom);
  }

  // if(spantxt=="ImageView"){
  //   // var typeDom = $('<i data-feather="menu"></i>');
  //   $("#" + treeNode.tId + "_span").html('<i data-feather="menu"></i>');
  // }

  if (treeNode.title || treeNode.desc) {
    let labelStr = treeNode.title || treeNode.desc
    if (labelStr.length > 17) {
      labelStr = labelStr.slice(0, 17) + '...'
      // labelStr.length = 17
    }
    var spanDom = document.createElement("span");
    spanDom.style = "display: inline-block;margin-left: 10px;color: #748094;";
    spanDom.innerHTML = labelStr
    $("#" + treeNode.tId + "_span")[0].appendChild(spanDom);
  }

  var detailDom = document.createElement("span");
  detailDom.innerHTML = ''
  detailDom.id = 'detail_btn_' + treeNode.nodeId
  detailDom.classList.add("details")
  detailDom.onclick = function () {
    clickTreeNode(treeNode)
    event.stopPropagation();
  }

  $("#" + treeNode.tId + "_span")[0].onclick = function () {
    clickTreeNode(treeNode)
    event.stopPropagation();
  }
  //
  // $("#" + treeNode.tId + "_span")[0].onmouseover = function () {
  //   // alert('1')
  //   $("#" + treeNode.tId + "_span")[0].classList.add("bg-gradient-warning")
  //   $("#" + treeNode.tId + "_span")[0].classList.add("shadow-dark-lg");
  //   handleMouseoverTree(treeNode)
  //
  //
  //
  //
  //   event.stopPropagation();
  // }
  // $("#" + treeNode.tId + "_span")[0].onmouseout = function () {
  //   $("#" + treeNode.tId + "_span")[0].classList.remove("bg-gradient-warning");
  //   $("#" + treeNode.tId + "_span")[0].classList.remove("shadow-dark-lg");
  //   handleMouseoutTree(treeNode)
  //   event.stopPropagation();
  // }
  $("#" + treeNode.tId + "_span")[0].classList = `tree-node-${treeNode.nodeId}`
  $("#" + treeNode.tId + "_span")[0].appendChild(detailDom);
}

function clickTreeNode(treeNode) {
    $("#sel_title_regx").val(treeNode.title)
    $("#sel_name_regx").val(treeNode.name)
    $("#sel_hwnd_regx").val(treeNode.hwnd)
    $("#sel_rect").val("["+treeNode.rect[0]+","+treeNode.rect[1]+","+treeNode.rect[2]+","+treeNode.rect[3]+"]");
    $("#sel_active").val(treeNode.is_active)
    $("#sel_visible").val(treeNode.is_visible)
    $("#sel_focus").val(treeNode.has_focus)
    $("#sel_status").val(treeNode.placement)

    var path = "http://"+host+api_tool_capture+"?hwnd="+ treeNode.hwnd+"&time="+new Date().getTime();

    //计算imageview 最大宽度
    var width = $(window).width() - ($("#filter_contain").width()+ $("#viewtree_contain").width());
    // alert(width)
    $("#win_huwn_show").css('max-width',(width-40)+"px");
    $("#win_huwn_show").attr('src',path)

    // alert(JSON.stringify(treeNode))

}

function filterwindows(){
    $("#win_cons").empty();

    var win_item = $(".hwnd_item")

    var f_title = $("#sel_title").prop('checked');

    var regx_str = $("#sel_title_regx").val();

    var regx = new RegExp(regx_str);

    var num = 0;

    for (const pos in nodes){
        var win = wins[pos];
        var item = win_item.clone();

        if(f_title){
            if(win.title == null|| win.title ==undefined || win.title=="" ){
                continue;
            }
        }

        if(regx_str != ""){
            if(!regx.test(win.title)){
                continue;
            }
        }

        num++;
        item.appendTo("#win_cons");
            // alert(win.title)
            // <li class="layui-menu-item-divider"></li>
        item.find(".hwnd_item_title").text(win.hwnd +" "+ win.title);

        item.tag = win.hwnd;

        item.attr('hwnd',win.hwnd);

        item.click(function (){
            var hwnd = $(this).attr('hwnd')
            var path = "http://"+host+api_tool_capture+"?hwnd="+ hwnd+"&time="+new Date().getTime();
            // alert(path)
            $("#win_huwn_show").attr('src',path)
        })
    }

    $("#hwnd_nums").text(num+"")

}