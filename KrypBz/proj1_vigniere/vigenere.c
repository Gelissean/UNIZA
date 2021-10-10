
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <time.h>

int myRand( int max )
{
  double r = (double) rand() / (double) RAND_MAX;
  return (int) ( max * r );
}

void getPassword( char *buffer, int length )
{
  int i;
  for ( i = 0; i < length; i++ )
  {
    buffer[i] = 'A' + myRand( 26 );
  }
  buffer[i] = '\0';
}


void encryptStream( FILE *inputStream, FILE *outputStream, const char *szPassword )
{
  int c;
  const char * p = szPassword;
  while ( ( c = fgetc( inputStream ) ) != EOF )
  {
    c = toupper(c);
    if ( c >= 'A' && c <= 'Z' )
    {
      int i = c - 'A';
      int j = *p - 'A';
      int k = ( i + j ) % 26;
      fputc( k + 'A', outputStream );
      
      // next character in pwd
      if (*++p == '\0' ) p = szPassword;
    }
    else
    {
      fputc( c, outputStream );
    }
  }
}

void encryptFile( const char *inputFileName, const char *outputFileName, const char *szPassword )
{
  FILE *inputStream = fopen( inputFileName, "r" );
  if ( inputStream != NULL )
  {
    FILE *outputStream = fopen( outputFileName, "w"  );
    if ( outputStream != NULL )
    {
      encryptStream( inputStream, outputStream, szPassword );
      fclose( outputStream );
    }
    fclose( inputStream );
  }
}

void decryptStream( FILE *inputStream, FILE *outputStream, const char *szPassword )
{
  int c;
  const char * p = szPassword;
  while ( ( c = fgetc( inputStream ) ) != EOF )
  {
    c = toupper(c);
    if ( c >= 'A' && c <= 'Z' )
    {
      int i = c - 'A';
      int j = *p - 'A';
      int k = ( i + 26 - j ) % 26;
      fputc( k + 'A', outputStream );
      
      // next character in pwd
      if (*++p == '\0' ) p = szPassword;
    }
    else
    {
      fputc( c, outputStream );
    }
  }
}

void decryptFile( const char *inputFileName, const char *outputFileName, const char *szPassword )
{
  FILE *inputStream = fopen( inputFileName, "r" );
  if ( inputStream != NULL )
  {
    FILE *outputStream = fopen( outputFileName, "w"  );
    if ( outputStream != NULL )
    {
      decryptStream( inputStream, outputStream, szPassword );
      fclose( outputStream );
    }
    fclose( inputStream );
  }
}

int main( int argc, char *argv[] )
{
  srand( time( NULL ) );

  char prefix[100];
  strcpy( prefix, "text1" );
  if ( argc > 1 ) strcpy( prefix, argv[1] );

  char inputFileName[200];
  strcpy( inputFileName, prefix ); 
  strcat( inputFileName, "_ascii.txt" );

  char encFileName[200];
  strcpy( encFileName, prefix ); 
  strcat( encFileName, "_enc.txt" );

  char decFileName[200];
  strcpy( decFileName, prefix ); 
  strcat( decFileName, "_dec.txt" );
  
  char szPassword[100];
  getPassword( szPassword, 20 + myRand( 10 ) );

  printf( "INPUT FILENAME: %s\n", inputFileName );
  printf( "ENCRYPTED FILENAME: %s\n", encFileName );
  printf( "DECRYPTED FILENAME: %s\n", decFileName );
  printf( "PASSWORD: %s\n", szPassword );
  
  encryptFile( inputFileName, encFileName, szPassword );
  decryptFile( encFileName, decFileName, szPassword );

  return 0;
}
