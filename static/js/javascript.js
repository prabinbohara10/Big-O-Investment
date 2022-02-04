function funda_radio(x){
    let de="";
    let mn="";
    let mx="";
    switch(x){
        case 1:
            de="bv_defined_id";
            mn="bv_min_id";
            mx="bv_max_id";
            break;
        case 2:
            de="bv_defined_id";
            mn="bv_min_id";
            mx="bv_max_id";
            break;
        case 3:
            de="eps_defined";
            mn="eps_min_id";
            mx="eps_max_id";
            break;
        case 4:
            de="eps_defined";
            mn="eps_min_id";
            mx="eps_max_id";
            break;
        case 5:
            de="mc_defined";
            mn="mc_min_id";
            mx="mc_max_id";
            break;
        case 6:
            de="mc_defined";
            mn="mc_min_id";
            mx="mc_max_id";
            break;       
        case 7:
            de="por_defined";
            mn="por_min_id";
            mx="por_max_id";
            break;
        case 8:
            de="por_defined";
            mn="por_min_id";
            mx="por_max_id";
            break;
        case 9:
            de="pb_defined";
            mn="pb_min_id";
            mx="pb_max_id";
            break;
        case 10:
            de="pb_defined";
            mn="pb_min_id";
            mx="pb_max_id";
            break;
        case 11:
            de="pe_defined";
            mn="pe_min_id";
            mx="pe_max_id";
            break;
        case 12:
            de="pe_defined";
            mn="pe_min_id";
            mx="pe_max_id";
            break;
        case 13:
            de="pgr_defined";
            mn="pgr_min_id";
            mx="pgr_max_id";
            break;
        case 14:
            de="pgr_defined";
            mn="pgr_min_id";
            mx="pgr_max_id";
            break;
        case 15:
            de="roa_defined";
            mn="roa_min_id";
            mx="roa_max_id";
            break;
        case 16:
            de="roa_defined";
            mn="roa_min_id";
            mx="roa_max_id";
            break; 
        case 17:
            de="roe_defined";
            mn="roe_min_id";
            mx="roe_max_id";
            break;
        case 18:
            de="roe_defined";
            mn="roe_min_id";
            mx="roe_max_id";
            break;
        case 19:
            de="rsi_defined_id";
            mn="rsi_min_id";
            mx="rsi_max_id";
            break;
        case 20:
            de="rsi_defined_id";
            mn="rsi_min_id";
            mx="rsi_max_id";
            break;
        case 21:
            de="ltp_defined_id";
            mn="ltp_min_id";
            mx="ltp_max_id";
            break;
        case 22:
            de="ltp_defined_id";
            mn="ltp_min_id";
            mx="ltp_max_id";
            break;}
    if(x%2==0){
        document.getElementById(mx).style.visibility="visible";
        document.getElementById(mn).style.visibility="visible";
        //document.getElementById(de).style.visibility="visible";
         document.getElementById(de).style.display="none";
        // document.getElementById(mn).disabled = false;
        // document.getElementById(mx).disabled = false;
        // document.getElementById(de).disabled = true;
    }else{
        document.getElementById(mn).style.visibility="hidden";
        document.getElementById(mx).style.visibility="hidden";
        
        document.getElementById(de).style.display="block";
        // document.getElementById(mn).disabled = true;
        // document.getElementById(mx).disabled = true;
        // document.getElementById(de).disabled = false;
    }
    // if(x==0){
    //     document.getElementById("ownn").style.visibility="visible";
    //     document.getElementById("predefined").style.display="none";
    // }else if(x==1){
    //     document.getElementById("ownn").style.visibility="hidden";
    //     document.getElementById("predefined").style.display="block";
    // }
    return;
}