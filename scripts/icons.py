"""Small local outline icon set. No remote assets or font dependency."""
PATHS = {
    'arrow': '<path d="M7 17 17 7M7 7h10v10"/>',
    'login': '<path d="M14 4h5v16h-5M3 12h12m-4-4 4 4-4 4"/>',
    'building': '<path d="m3 9 9-6 9 6H3Zm2 2v7m5-7v7m4-7v7m5-7v7M3 21h18"/>',
    'shield': '<path d="m12 3 8 3v6c0 5-8 9-8 9s-8-4-8-9V6l8-3Z"/><path d="m8 12 3 3 5-6"/>',
    'chat': '<path d="M21 11a9 9 0 0 1-9 9 10 10 0 0 1-4-.8L3 21l1.5-5A9 9 0 1 1 21 11Z"/><path d="M8 11h.01M12 11h.01M16 11h.01"/>',
    'digital': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8m-4-4v4m-2-13 5 3-5 3V8Z"/>',
    'box': '<path d="m12 3 9 5v9l-9 5-9-5V8l9-5Zm0 9 9-4M3 8l9 4v10M7.5 5.5l9 5V15"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'vision': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'pin': '<path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2"/>',
    'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
}
def icon(name):
    return '<svg class="icon icon-'+name+'" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'+PATHS[name]+'</svg>'
