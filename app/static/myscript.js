$(document).ready(function(){
//增加一行
$(".addrow").click(function(){
	var goods_quantity=$("#quantity").val();
	var goods_name=$("#goods").val();
	if(!isNaN(goods_quantity) && goods_quantity!=""){
	var xuhao=getxuhao();
	var insert_html="<tr><td name=\"xuhao\">"+xuhao+"</td><td class=\"goods_name\"><input type=\"text\" name=\"goods_name\" readonly=\"true\" value=\""+goods_name+"\"></td><td class=\"goods_quantity\"><input type=\"text\" name=\"goods_quantity\" value=\""+goods_quantity+"\"></td><td><input type=\"checkbox\" name=\"ckb\"></td></tr>";
	$("#tbfoot").before(insert_html);
	count_quan();
	$("#quantity").val("");
	}else{
		alert("警告，数量请输入数字！");
		$("#quantity")[0].focus();
	}
});
//删除勾选的行
$(".delrow").click(function(){
	//$(this).parentsUntil("tr").empty();
	//$(this).parent().parent().remove();
	var ckbs=$("input[name='ckb']:checked");
	if(ckbs.size()==0){
        	    alert("要删除指定行，需选中要删除的行！");
                  return;
     	}
     	ckbs.each(function(){
     	    $(this).parent().parent().remove();
     	});
     	getxuhao();
		count_quan();
});
//全选or全不选
$("#ckall").click(function(){
	var isChecked=$(this).prop("checked");
	$("input[name='ckb']").prop("checked",isChecked);
	/*
	if(this.checked){
		$("input[name='ckb']").attr("checked",true);
		$(this).attr("checked",true);
	}else{
		$("input[name='ckb']").attr("checked",false);
		$(this).attr("checked",false);
	}
	*/
});
$(".form_post").click(function(){
	$("#quantity").val("0");
	$("form").submit();

	//alert($(".goods_quantity"));
	//$("form").submit({goods_quantity:$(".goods_quantity").text()});
	/*
	$(".goods_name").each(function(){
		alert($(this).text());
	});
	*/
});
//匹配ready()
});
//配置序号
function getxuhao(){
	var i=1;
	$("td[name='xuhao']").each(function(){
		$(this).text(i);
		i=i+1;	
	});
	return i;
}
//统计数量
function count_quan(){
	var count_num=0;
	$("input[name='goods_quantity']").each(function(){
		count_num=count_num+Number($(this).val());
	});
	$("#the_count").val(count_num);
}