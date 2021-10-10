program Kassisk;

var pole : array [0..32768] of char;
    len : integer;
    t : text;
    c : char;
    i, j : integer;
    s: string;

begin
  len := 0;
  assign(t, 'text1.txt');
  reset(t);
  while (not eof(t)) do begin
    read(t, c);
    if (c >= 'A') and (c <= 'Z') then begin
      pole[len] := c;
      inc(len);
    end;
  end;
  close(t);

  writeln(pole);
  writeln;
  
  for i := 0 to len - 3 do begin
    for j := i + 1 to len - 3 do begin
      if (pole[i] = pole[j]) and (pole[i+1] = pole[j+1]) and (pole[i+2] = pole[j+2]) then 
      begin
        s := pole[i] + pole[i+1] + pole[i+2];
        write(j - i, ' (', s, '), ');
      end;
    end;
  end;
  
  writeln;
   
end.
