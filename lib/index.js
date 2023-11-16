const bindings = require('bindings')

let binding = {}
try {
    binding = bindings('binding.node')
} catch (e) {
    //
}

module.exports = exports = binding;
