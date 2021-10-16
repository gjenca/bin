#!/usr/bin/perl
use Getopt::Std;
use Env;

sub Xecute{

my $handle=shift(@_);

$command='';
while ($line=<handle>) {
	$command=$command.$line;
}
eval($command);

}


getopt("hbfsSn");

if (not $opt_h) {$opt_h='header';}
if (not $opt_b) {$opt_b='body';}
if (not $opt_f) {$opt_f='footer';}
if (not $opt_S) {$opt_S='g_setup.pl';}
if (not $opt_s) {$opt_s='setup.pl';}


if (open(handle,"<".$opt_S)) {
# Perform a global setup

Xecute(handle);

close(handle);
}

#printf "%s\n",eval("$setup_var");

# Now write the header

if (open(handle,"<".$opt_h)) {

while ($line=<handle>) {
	while($line=~s/^(.*)<## *(.*) *##>(.*)$/$1.eval('$'.$2).$3/e){};
	print $line;
}
close(handle);
}

for ($linenr=1;not $opt_n or $linenr<=eval($opt_n);$linenr++) {

if (open(handle,"<".$opt_s)) {

# Perform a row (body) setup
$exit=0;
Xecute("ahhah");
close(handle);
if ($exit) {
	last;
}
}

if (open(handle,"<".$opt_b)) {

while ($line=<handle>) {
	while($line=~s/^(.*)<##([^\$]*)\$\[(.*)\](.*)##>(.*)$/eval('$'.$3) ? $1.$2.eval('$'.$3).$4.$5: $1.$5/ge){};
	print $line;
}

}
	else {
		last;
	}
}

# Now write the footer

if (open(handle,"<".$opt_f)) {

while ($line=<handle>) {
	while($line=~s/^(.*)<## *(.*) *##>(.*)$/$1.eval('$'.$2).$3/e){};
	print $line;
}
close(handle);
}

