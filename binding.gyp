{
	"targets": [{
        "conditions": [
			['OS=="mac"',
			{
            "target_name": "binding",
            "include_dirs": ["<!(node -e \"require('nan')\")"],
            "sources":[
                "src/clip_osx.h",
                "src/clip_osx.mm"
            ],
			'defines': [
				'__MACOSX_CORE__',
                '__MAC__'
			],
			'link_settings': {
				'libraries': [
                    '-framework Cocoa',
					'-framework CoreFoundation',
				]
			},
			'xcode_settings': {
				'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
				'OTHER_CFLAGS': [
					'-ObjC++',
					'-std=c++17'
				]
			    }
			}
			],
			['OS=="win"',
			{
            "target_name": "binding",
            "include_dirs": ["<!(node -e \"require('nan')\")"],
            "sources":[
                "src/clip_win.h",
                "src/clip_win.cc"
            ],
            'defines': [
				'__WIN32__'
			]
            }
			],
			['OS=="linux"',
				{}
			]
		]
	}]
}
