create table snippets (
keyword text primary key,
message text not null default '',
hidden boolean not null default false
);
