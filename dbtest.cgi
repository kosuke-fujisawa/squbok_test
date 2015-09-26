#!/usr/bin/perl -w

# エラーをブラウザに表示
use CGI::Carp qw(fatalsToBrowser);
# DBIモジュール
use DBI;
use strict;
use warnings;

# ユーザ名とパスワード
$user = 'root';
$pass = 'c10u691214';

# DBへ接続
$db = DBI->connect('DBI:mysql:mysql', $user, $pass);

# 命令
$sth = $db->prepare( "select * from LOGIN" );

# 実行
$sth->execute;

# 出力
print "Content-type: text/html\n\n";
while( @row = $sth->fetchrow_array ){
	print "@row\n";
}

$db->disconnect;

exit;

