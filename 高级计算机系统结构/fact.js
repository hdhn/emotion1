function disp(m) {
    console.log(m);

}
function disChar(c) {
    disp(String.fromCharCode(c));

}
function  interp(code) {
    let data = new Array(30000).fill(0);
    let ptr = 0;
    let pc = 0;
    let stack = new Array();
    let bracket_count = 0;
    let skip_loop = false;
    while(pc<code.length()){
        let c = code[pc];
        if(skip_loop === true){
            if (c === '['){
                bracket_count++;
            }else if(c ===']'){
                bracket_count--;
                if (bracket_count === 0){
                    skip_loop = false;
                }
            }
            pc++;
            continue;
        }
        switch(c){
            case '>':
                ptr++;
                pc++;
                break;
            case '<':
                ptr--;
                pc++;
                break;
            case '+':
                data[ptr]++;
                pc++;
                break;
            case '-':
                data[ptr]--;
                pc++;
                break;
            case '.':
                disp(data[ptr]);
                pc++;
                break;
            case ',':
                pc++;
                break;
            case '[':
                if(data[ptr] === 0){
                    bracket_count = 1;
                    skip_loop = true;
                    pc++;
                }else{
                    pc++;
                    stack.push(pc)
                }
                break;
            case ']':
                if(data[ptr] === 0){
                    pc++;
                    stack.pop()
                }else {
                    pc = stack[stack.length - 1];
                }
        }
    }

}
interp('+++++.');
interp('++++++>++[-<+>]<.');