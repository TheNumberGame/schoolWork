$(document).ready(function(){
	$(".a1").click(function(){
		$.post("/Q",{ question: "Yes"});
		$(".a1").hide(function(){
			$("#pr1").show(function(){
				$("#q2").show();
				$(".a2").show(function(){	
					$("#n2").click(function(){
						$.post("/Q",{ question: "No"});
						$(".a2").hide();
						$("#pr21").show(function(){
							$("#q3").show();
							$(".a3").show(function(){	
								$("#n3").click(function(){
									$.post("/Q",{ question: "No"});
									$(".a3").hide();
									$("#pr31").show();
									$("#b1").show();
								});
								$("#y3").click(function(){
									$.post("/Q",{ question: "Yes"});
									$(".a3").hide();
									$("#pr3").show();
									$("#b1").show();
								});
							});
						});
					});
					$("#y2").click(function(){
						$.post("/Q",{ question: "Yes"});
						$(".a2").hide();
						$("#pr2").show(function(){
							$("#q3").show();
							$(".a3").show(function(){	
								$("#n3").click(function(){
									$.post("/Q",{ question: "No"});
									$(".a3").hide();
									$("#pr31").show();
									$("#b1").show();
								});
								$("#y3").click(function(){
									$.post("/Q",{ question: "Yes"});
									$(".a3").hide();
									$("#pr3").show();
									$("#b1").show();
								});
							});
						});
					});
				});
			});
		});
	});
	$("#b1").click(function(){
		$("#table1").hide();
		$("img").show();
	});
});
