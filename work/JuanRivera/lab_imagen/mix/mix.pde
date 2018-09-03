void setup() //<>//
{
  PImage lenaI = loadImage("lena.jpg");
  PImage plazaI = loadImage("plaza.png");
  PImage finalI = createImage(plazaI.width,plazaI.height,0);
  int factor = 0;
  finalI.loadPixels();
  size(390,580);
  for (int i = 0;i < plazaI.height;i++)
  {
    for (int j = 0; j < plazaI.width;j++)
    {
      color a = plazaI.get(j,i);
      color b = lenaI.get(j,i);
      finalI.pixels[i*plazaI.width+j] = int(red(a)+green(a)+blue(a));
      
    }
  }
  image(finalI,0,0);
}
