void setup() //<>//
{
  PImage lenaI = loadImage("lena.jpg");
  PImage plazaI = loadImage("plaza.png");
  PImage finalI = createImage(plazaI.width,plazaI.height,0);
  int factor = 127;
  finalI.loadPixels();
  plazaI.loadPixels();
  size(390,580);
  for (int i = 0;i < plazaI.height;i++)
  {
    for (int j = 0; j < plazaI.width;j++)
    {
      color a = plazaI.get(j,i);
      color b = lenaI.get(j,i);
      finalI.pixels[i*plazaI.width+j] = color(red(b),green(b),blue(b),factor);
      plazaI.pixels[i*plazaI.width+j] = color(red(a),green(a),blue(a),256-factor);
      
    }
  }
  image(finalI,0,0);
  image(plazaI,0,0);
  save("mix.jpg");
}
