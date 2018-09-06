PImage img;
PImage im;


void setup() 
{
  size(378,568);  
  img = loadImage("plaza.png");
  im = loadImage("lena.jpg");
  image(img,0,0);

  im.loadPixels();
  for (int x = 0; x < im.pixels.length; x++) {
      
      //leemos el valor de los canales rojo, verde y azul de cada uno
      float r = red( im.pixels[x]);
      float g = green(im.pixels[x]);
      float b = blue(im.pixels[x]);
      //asignamos esos mismos valores a cada píxel
      im.pixels[x]= color(r,g,b,126);
      
    
  }
    image(im,0,0);
  updatePixels();
  
  
}