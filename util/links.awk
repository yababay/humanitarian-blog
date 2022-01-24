BEGIN {
    mute = 1
    first_header = 1
    first_empty = 1
    first_medium = 1
}

/^Михаил Беляков/ { mute = 1; next}
/More from/       { mute = 1; next}
/Скрытых ссылок/  { mute = 1; next}
/Видимых ссылок/  { mute = 0; print "\n## Ссылки\n"; next}
/^\S/ {
   if (first_header == 1) { 
      first_header = 0; 
      mute = 0; 
      print "# " $_ "\n"; 
      print ""
      match(ARGV[1], /^([0-9\-]{10}).*/, arr)
      print "<p class=\"text-end time-holder\"><time>"arr[1]"</time></p>"
      print ""
      next
   }
   else next
}

{
    if (mute == 1) { next }
}

/wikipedia\.org/   { match($_, /.*(https:\/\/.*)$/, arr); print "1. [Статья в Википедии]("arr[1]")";     next }
/telegra\.ph\/\S+/ { match($_, /.*(https:\/\/.*)$/, arr); print "1. [Публикация в Telegraph]("arr[1]")"; next }
/signin\?operation=.*yababay\.medium\.com/  { 
    if(first_medium == 0) next
    first_medium = 0
    match($_, /.*(https:\/\/yababay[^&]+)/, arr); 
    print "1. [Публикация в Medium]("arr[1]")"
    next
}

/\(BUTTON\)/                            { next }
/^\s+[0-9]+\.\s+(file|http|https):\/\// { next }
/^\s+[0-9]+\.\s+android-app/            { next }
/Михаил.*Беляков/                       { next }
/Originally published at/               { next }
/[0-9]\s+min read/                      { next }

/^$/ {
    if(first_empty == 0) { first_empty = 1; print "" }
    else next 
}

{gsub(/\[[0-9]+\]/, "", $_)}

/https:\/\/(www\.)?youtube\.com/ {
    sub(/^   /, "", $_)
    print "<iframe width=\"790\" height=\"444\" src=\""$_"\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
    next
}

/^\s{6,}/ { print ; next }

/^\s+/ {
    first_empty = 0
    sub(/^     /, "> ", $_)
    sub(/^    1\./, "\n1.", $_)
    sub(/^    /, "", $_)
    sub(/^   /, "", $_)
    print $_  
}

END {
    print ""
}
