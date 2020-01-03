function setVisibility(id) {
if(document.getElementById('bt1').value=='Hide Layer'){
document.getElementById('bt1').value = 'Upload CSV files';
document.getElementById(id).style.display = 'none';
}else{
document.getElementById('bt1').value = 'Hide Layer';
document.getElementById(id).style.display = 'flex';
}

document.getElementById('buttonID').addEventListener('click', openDialog);

function openDialog(id) {
  document.getElementById(id).click();
  
}
}



