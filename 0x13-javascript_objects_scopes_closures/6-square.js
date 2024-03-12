#!/usr/bin/node
class Square extends Rectangle{

	constructor(size){
		this.size = size;
		super(this.size, this.size);

	}


	charPrint(c = 'X'){
 		for (let i = 0; i < this.height; i++) {
            let row = '';
            for (let j = 0; j < this.width; j++) {
                row += c;
            }
            console.log(row);
        }

	}
}
