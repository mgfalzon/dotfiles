set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" My Plugins
Plugin 'jreybert/vimagit'           "git
Plugin 'preservim/nerdtree'         "treeview
Plugin 'vifm/vifm.vim'              "file manager
Plugin 'sheerun/vim-polyglot'       "language support
""Plugin 'dense-analysis/ale'       "sytax support/linting
Plugin 'alvan/vim-closetag'         "close html tags
Plugin 'chriskempson/base16-vim'    "base16 colors
Plugin 'vim-scripts/vim-auto-save'  "autosave
Plugin 'junegunn/fzf.vim'           "ctrl p
Plugin 'godlygeek/tabular'          "Tables
Plugin 'plasticboy/vim-markdown'    "Markdown

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"
" Plugin Settings
map <C-b> :NERDTreeToggle<CR>
map <Leader>e :Vifm<CR>
map <Leader>s :AutoSaveToggle<CR>
map <C-o> :Buffers<CR>


call system('!git rev-parse --is-inside-work-tree')
if v:shell_error == 0
  noremap <silent> <C-p> :GFiles --cached --others --exclude-standard<CR>
else
  noremap <silent> <C-p> :Files<CR>
endif

let g:vim_markdown_new_list_item_indent = 2

"Basic Settings"
set nocompatible
inoremap jj <Esc>
syntax on
set hidden
set mouse=a
set smartindent
set clipboard=unnamed
set wrap!

"Spacing"
set expandtab
set ts=2 sw=2
"au Filetype markdown setl ts=2 sw=2
"au Filetype python setl ts=2 sw=2

"Splits"
set splitbelow splitright
inoremap <C-h> <C-w>h
inoremap <C-j> <C-w>j
inoremap <C-k> <C-k>k
inoremap <C-l> <C-l>l

"Close Quotes/Parens"
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>

if filereadable(expand("~/.vimrc_background"))
  let base16colorspace=256
  source ~/.vimrc_background
endif
