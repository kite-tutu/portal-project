function my_auto_fill_func(){
    
    if (document.getElementById('emp_id').value != "")
    {
        document.getElementById('mem_id').value = document.getElementById('emp_id').value.zfill(10)  
    }
}
