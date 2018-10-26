String media_path = "../../media/";
String out_path = "../../out/";

void setup() {
  PImage img = loadImage(media_path + "plaza.png");
  PImage img2 = loadImage(media_path + "lena.jpg");
   
  size(378, 568);
  background(0);
  img.loadPixels();
  img2.loadPixels();
  
  for (int y=0; y<img2.height; y++) {
    //Parametro que se usa para controlar la transparencia entre las dos imagenes. Importante: Esta dado en porcentaje y hace referencia a la plaza.
    //Ej. Si parameter = 100. Solo se veria la plaza. Si parameter = 50, la transparencia daria igual de importancia a cada imagen. Si parameter = 0 solo se veria a lena.
    int parameter = 50;
    
    for (int x=0; x<img.width; x++) {
      color c1 = img.get(x,y);
      color c2 = img2.get(x,y);
      
      img.set(x,y, color( (red(c1)*parameter)/100 + (red(c2)*(100-parameter))/100, (green(c1)*parameter)/100 + (green(c2)*(100-parameter))/100, (blue(c1)*parameter)/100 + (blue(c2)*(100-parameter))/100));
    }
  }
  image(img, 0, 0);
}
