String media_path = "../../media/";
String out_path = "../../out/";

void setup(){
  /*-------------------------------
  creamos un array para almacenar la paleta de colores
  sepia. El color de la paleta se calcula por cada banda
  en un rango desde cero hasta el valor maximo definido en 
  las variables r,g,b.
  */
  color[] palette = new color[256];
  int r = 255;
  int g = 240;
  int b = 192;
  for (int i=0; i<palette.length; i++) {
    palette[i] = color(r*i/255, g*i/255, b*i/255);
  }
  //----------------------------

  PImage img = loadImage(media_path + "lena.jpg");
  size(512, 512);
  
  //Creamos el buffer de pixeles de la imagen
  img.loadPixels();

  for (int i=0; i< img.pixels.length; i++) {
      color c = img.pixels[i];
      
      //calculamos un valor promediado de las tres bandas de
      //color de la imagen.
      float gray = (red(c)+green(c)+blue(c))/3;
      
      //Aproximamos el color obtenido al color de la paleta
      img.pixels[i] = palette[int(gray)];
  }
  //Acualizamos la imagen.
  img.updatePixels();
  
  //Dibujamos la imagen en pantalla
  image(img, 0, 0);
  saveFrame(out_path + "lena-sepia.jpg");
}
