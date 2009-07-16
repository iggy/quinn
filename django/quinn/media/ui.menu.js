/*
 * jQuery UI Draggable
 *
 * Copyright (c) 2008 Paul Bakaus
 * Dual licensed under the MIT (MIT-LICENSE.txt)
 * and GPL (GPL-LICENSE.txt) licenses.
 * 
 * http://docs.jquery.com/UI/Menu
 *
 * Depends:
 *	ui.core.js
 */
(function($) {

$(document).ready(function() {
	$(document).bind('click', function(event) {
		$.ui.menu.prototype.closeAll(event);
	});
});

$.widget("ui.menu", {

	_init: function() {

		var o = this.options;
		$.extend(this, {
			_showTimers: [],
			_hideTimers: []
		});

		//Prepare a nodelist of list items that's not in the DOM (anymore)
		if(o.items.constructor == String) {
			this.items = $(this.options.items, this.element).length ? $(this.options.items, this.element).remove() : $(this.options.items).remove();
		} else {
			this.items = o.items.length ? o.items.remove() : this._generateMarkupFromJSON(o.items);
		}

		//Create the actual wrapping menu and append the markup
		this._createMenu();

	},

	_generateMarkupFromJSON: function(json, cache) {

		var html = $('<ul></ul>');
		if($.isFunction(json)) {
			json.cache = cache;
			return html.data('menu-ajax', json);
		}

		for(var i in json) {
			var item = $('<li><a href="#">'+i+'</a></li>').appendTo(html);
			if(json[i].items) item.append(this._generateMarkupFromJSON(json[i].items, json[i].cache));

		}

		return html;

	},

	_createMenu: function() {

		var o = this.options, self = this;

		this.menu = $('<div class="ui-component ui-component-content"></div>')
			.css({ width: o.width })
			.append(this.items.addClass('ui-menu')) //Append the actual item structure
			.appendTo(o.mode == 'static' ? this.element : (o.appendTo == 'element' ? this.element : o.appendTo)); //Append to the selected element, otherwise to this.options.appendTo (body by default)

		//If the menu should be rendered to the page statically, add a wrapper class that positions it absolutely
		if(o.mode != 'static')
			this.menu.addClass('ui-menu-container');

		//Attach hover states for items
		this._attachHoverStates(this.items);

		// when there are multiple levels of hierarchy, create flyout or drilldown menu
		if ($('ul', this.items).length) {
			if(this.options.type == 'drilldown')
				this._prepareDrilldown();
			if(this.options.type == 'flyout')
				this._prepareFlyout();
		}

		this.items.css('visibility', 'visible');
		if(this.menu.css('position') != 'absolute' && this.options.type != 'drilldown') //If the position isn't absolute,
			this.menu.css('position', 'absolute').height(this.menu.height()).css('position', 'relative');  //set a hard value for the height 


		if(o.mode != 'static') {

			if(o.mode == 'dropdown') {
				this.element.bind('click', function(event) {
					self.toggle(event);
				});
			}

			if(o.mode == 'context') {
				this.element.bind('contextmenu', function(event) {
					self.open(event);
					event.preventDefault();
				});
			}

			//Hide the menu, until it is shown
			this.menu.hide();
		}

	},

	_itemOver: function(item, event) {

		var item = $(item), self = this;
		item
			.addClass(this.options.hoverClassSecondary)
			.find('a:eq(0)').addClass(this.options.hoverClass +' ui-menu-item-on').focus();


		if(this.options.type == 'flyout' && item.is(':has(ul)')) {

			var subList = $('> ul', item);

			for (var i=0; i < this._hideTimers.length; i++) {
				if(this._hideTimers[i][1][0] == subList[0]) clearTimeout(this._hideTimers[i][0]);
			};

			if(subList.data('menu-ajax')) {

				item.find('a > span').removeClass('ui-arrow-right-default').addClass('ui-loading-right-default'); //Use loading indicator instead of arrow
				subList.data('menu-ajax').apply(this.element, [function(markup) {

					subList.empty();
					self.add(markup, item, 'append');
					item.find('a > span').removeClass('ui-loading-right-default').addClass('ui-arrow-right-default');

					//If we want to cache it, remove the ajax binding when it's called once
					if(subList.data('menu-ajax').cache) subList.data('menu-ajax', false);

					self._showTimers.push([setTimeout(function(){
						subList.addClass('ui-component-content').show();
						subList.positionAround(event, {
							around: subList.parent(),
							direction: 'right',
							offset: [0,-1]
						});
						self._trigger('browse', event, { item: subList });
					}, 0), subList]);

				}, { item: item }]);


			} else {

				this._showTimers.push([setTimeout(function(){
					subList.addClass('ui-component-content').show();
					subList.positionAround(event, {
						around: subList.parent(),
						direction: 'right',
						offset: [0,-1]
					});
					self._trigger('browse', event, { item: subList });
				}, this.options.flyoutDelay), subList]);

			}



		}

	},

	_itemOut: function(item, event) {

		var item = $(item), self = this;
		item
			.removeClass(this.options.hoverClassSecondary)
			.find('> a').removeClass(this.options.hoverClass +' ui-menu-item-on').blur();


		if(this.options.type == 'flyout' && item.is(':has(ul)')) {

			for (var i=0; i < this._showTimers.length; i++) {
				if(this._showTimers[i][1][0] == $('> ul', item)[0]) clearTimeout(this._showTimers[i][0]);
			};

			this._hideTimers.push([setTimeout(function(){
				$('> ul', item).removeClass('ui-component-content').hide();
			}, this.options.flyoutDelay), $('> ul', item)]);

		}

	},

	_attachHoverStates: function(items, andSelf) {

		var self = this, items = andSelf ? $('li', items).add(items) : $('li', items);
		items.each(function() {
			if(!$.data(this, 'menu-hover-attached')) {
				$(this)
					.data('menu-hover-attached', true)
					.hover(function(event) {
						self._itemOver(this, event);
					}, function(event) {
						self._itemOut(this, event);
					});
			}
		});

	},

	_resetDrilldown: function(stayOpen) {

		this.breadcrumb.empty().append(this.crumbDefaultHeader);
		$('.ui-menu-current', this.menu).removeClass('ui-menu-current');
		if (!stayOpen) { this.menu.find('.ui-menu-dd ul').css({ visibility: 'hidden' }); }

	},

	_refreshDrilldownHeight: function() {

		// standardize all menu heights & widths so that they cover the previous menu completely
		var listHeights = [];
		this.items.find('ul').each(function(i){ listHeights[i] = $(this).height(); });
		listHeights.sort(function(a, b) { return b - a; });
		this.items.find('ul').css({ height: listHeights[0], width: this.options.width });

		// apply scrollbar to the menu when it exceeds max height
		if (listHeights[0] > this.options.maxHeight) {
			this.menu
				.find('.ui-menu-dd')
				.addClass('ui-menu-scroll')
				.css({ height: this.options.maxHeight, overflow: 'auto', 'overflow-x': 'hidden' })
					.find('ul')
					.css({ width: this.options.width - 16 });
		} else {
			this.menu
				.find('.ui-menu-dd')
				.css({ height: listHeights[0] }).find('ul').css({ width: this.options.width });
		};

	},

	_prepareDrilldown: function() {


		var self = this;

		this.breadcrumb = $('<ul class="ui-menu-dd-breadcrumb ui-component-content"></ul>');
		this.crumbDefaultHeader = $('<li class="ui-menu-dd-text">'+this.options.crumbDefaultText+'</li>');

		if (!this.items.is('.ui-menu-dd')) {

			this.menu
				.css({ overflow: 'hidden' })
				.find('ul').addClass('ui-component-content');

			this.items
				.addClass('ui-menu-dd ui-menu-current')
				.find('ul').css({ width: this.options.width });

			// set up links to be split-button (selectable nodes + navigation links) or single button (navigation only)
			this.items.find('a').each(function(){
				if($(this).next().is('ul')) {
					if (self.options.selectCategories) {
						$(this).addClass('ui-menu-split-btn').html('<span>'+ $(this).text()+'</span>')
							.after('<a href="#" class="ui-menu-nextlevel"><span class="'+self.options.nextMenuClass+'">View next level &gt;</span></a>');
					}
					else {
						$(this).addClass('ui-menu-indicator').html('<span class="'+self.options.nextMenuClass+'">'+ $(this).text()+'</span>');
					};
				};
			});


			this._refreshDrilldownHeight();

		};


		this.options.backLink ? this.breadcrumb.addClass('ui-menu-footer').appendTo(this.menu) : this.breadcrumb.addClass('ui-menu-header').prependTo(this.menu);
		this.breadcrumb.append(this.crumbDefaultHeader);


		$('a', this.items).bind('click.menu', function(event){
			if ($(this).is('.ui-menu-indicator') || $(this).is('.ui-menu-nextlevel')) {
				self._nextDrilldownLevel(this, event);
				return false;
			}
			else {
				self._choose($(this.parentNode), event);
				return false;
			};
		});

	},

	_nextDrilldownLevel: function(el, event){

		var thisLink = $(el),
			thisList = thisLink.parents('ul:eq(0)'),
			nextList = thisLink.next(),
			firstCrumbText = this.options.backLink ? this.options.backLinkText : this.options.topLinkText,
			firstCrumbClass = this.options.backLink ? 'ui-menu-prev-list ui-arrow-left-default' : 'ui-menu-all-lists',
			firstCrumb = $('<li class="'+firstCrumbClass+'"><a href="#">'+firstCrumbText+'</a></li>'),
			self = this
		;

		// first breadcrumb link
		if (this.breadcrumb.find('li').size() == 1){

			this.breadcrumb.empty().append(firstCrumb);

			// 'back' link
			if (firstCrumb.is('.ui-menu-prev-list')) {

				$('.ui-menu-prev-list a', this.menu).bind('click.menu', function(){

					$('.ui-menu-current', this.menu).animate({ left: self.options.width }, self.options.crossSpeed);
					if ($('.ui-menu-current', this.menu).parents('ul').eq(0).is('.ui-menu')) { 
						self._resetDrilldown(true);
					} else {
						$('.ui-menu-current', this.menu)
							.removeClass('ui-menu-current')
							.parents('ul').eq(0).addClass('ui-menu-current');
					};
					return false;

				});

			} else if (firstCrumb.is('.ui-menu-all-lists')) { 	// standard breadcrumb

				$('.ui-menu-all-lists a', this.menu).bind('click.menu', function(){
					self.menu.find('ul').not('.ui-menu, .ui-menu-dd-breadcrumb').animate({ left: self.options.width }, self.options.crossSpeed);
					if ($(this).next().is('span')) { $(this).next().remove(); }
					self._resetDrilldown(true);
					return false;
				});

			};

		};


		//Add a new crumb if we don't have a single back link
		if (!self.options.backLink) {

			//Remove the current crumb class from the other crumbs
			$('li.ui-menu-current-crumb', this.menu).removeClass('ui-menu-current-crumb');

			var crumbText = (thisLink.prev().is('a')) ? thisLink.prev().text() : thisLink.text();
			var newCrumb = $('<li class="ui-menu-current-crumb" style="display: none;"><a href="javascript://" class="ui-menu-crumb">'+crumbText+'</a></li>')
				.appendTo(self.breadcrumb).prev().append(' <span>&gt;</span>');

			newCrumb.show().find('a').bind('click.menu', function(event){

				if ($(this).parent().is('.ui-menu-current-crumb')){
					self._choose($(this.parentNode), event);
					return false;
				}
				else {
					nextList.find('ul').animate({ left: self.options.width }, self.options.crossSpeed);
					$(this).parent().nextAll().css({ visibility: 'hidden' }).slideUp(self.options.crossSpeed, function(){$(this).remove();});
					$(this).parent().addClass('ui-menu-current-crumb').find('a').next().remove();
					self._trigger('browse', event, { item: null }); //TODO: Reference to item
					return false;
				};

			});

		}


		// show the next list
		$('.ui-menu-current', this.menu).removeClass('ui-menu-current');
		nextList.css({ visibility: 'visible', left: self.options.width })
			.animate({ left: 0 }, self.options.crossSpeed)
			.addClass('ui-menu-current');

		self._trigger('browse', event, { item: nextList });

	},

	_attachFlyoutStyles: function(item) {

		item.style.position = 'relative';
		var showTimer, hideTimer, self = this;
		var sublists = $('ul', item); //select all sub lists from this point

		sublists
			.css({
				position: 'absolute',
				top: -1,
				left: this.options.width, //Show them at the left of the preceding list
				width: this.options.width, //Set the width according to the options
				visibility: 'visible' })
			.hide();


		$('> a', item)
			.addClass('ui-menu-indicator') //Add a class that shows the little arrow to indicate a sub list
			.html('<span class="'+self.options.nextMenuClass+'">'+$('> a', item).text()+'</span>'); //Insert a new span

	},

	_prepareFlyout: function() {


		var self = this;
		this.items.addClass('ui-menu-flyout');

		 //Find all li's that have sub lists and attach behaviour to them
		this.menu.find('li:has(ul)').each(function() {
			self._attachFlyoutStyles(this);
		});

		//Attach the choose click handler to all list items
		$('a', this.menu).bind('click', function(event){
			self._choose($(this.parentNode), event);
			event.preventDefault();
		});

	},

	remove: function(position) {
		$(position, this.items).remove();
	},

	replace: function(item, position) {

		var old = $(position, this.items);
		if(old.length) return;
		
		this.add(item, position, 'before');
		old.remove();

	},

	add: function(item, position, type) {

		var self = this;
		var item = $(item.constructor == String || item.jquery ? item : this._generateMarkupFromJSON(item));

		if(type != 'append') { //We want to have it before/after a node
			$(position, this.items)[type](item);
		} else {

			if(!$(position, this.items).find('ul').length) {
				$(position, this.items).append('<ul></ul>');
				this._attachFlyoutStyles($(position, this.items)[0]);
			}

			//We have to remove the outer ul that served as a wrapper, because we already have a ul
			if(item.is('ul')) item = $('> *', item);
			$(position, this.items).find('ul:eq(0)').append(item);

		}


		if(this.options.type == 'drilldown') {



		} else { //It's a flyout menu item

			this._attachHoverStates(item, true);

			//Find all li's that have sub lists and attach styling to them
			if(item.is(':has(ul)')) this._attachFlyoutStyles(item[0]);
			item.find('li:has(ul)').each(function() { self._attachFlyoutStyles(this); });

			//Attach the choose click handler to all list items
			$('a', item).bind('click', function(event){
				self._choose($(this.parentNode), event);
				event.preventDefault();
			});

		}

	},

	toggle: function(event) {
		return this[this.visible ? 'close' : 'open'](event);
	},

	open: function(event) {

		if(this.options.exclusive) {
			this.closeAll();
		}

		this.menu.show();
		this.menu.positionAround(event, {
			around: this.options.mode == 'context' ? 'mouse' : this.element,
			direction: this.options.direction
		});

		$.ui.menu.manager.push(this);
		this.visible = true;
		this._trigger('open', event, { });

	},

	closeAll: function(excludeEvent) {

		var exclusion = null;
		if(excludeEvent) {
			var q = $(excludeEvent.target).parents().andSelf().each(function() {
				if($.data(this, 'menu') && ($.data(this, 'menu').options.mode == 'context' ? excludeEvent.which == 3 : true)) exclusion = $.data(this, 'menu');
			});
		}

		for (var i=0; i < $.ui.menu.manager.length; i++) {
			if(exclusion != $.ui.menu.manager[i]) $.ui.menu.manager[i].close(excludeEvent);
		};

	},

	close: function(event) {

		if(this.options.type == 'drilldown' && this.options.mode == 'static')
			return;

		this.menu.hide();
		for (var i=0; i < $.ui.menu.manager.length; i++) {
			if($.ui.menu.manager[i] == this) $.ui.menu.manager.splice(i,1);
		};
		this.visible = false;
		this._trigger('close', event, { });

	},

	_choose: function(item, event) {

		this.close(event);
		this._trigger('choose', event, { item: item });

	}

});

$.extend($.ui.menu, {
	manager: [],
	defaults: {
		type: 'flyout', //Can be set to either flyout, drilldown or toolbar
		mode: 'static', //Can be set to context (open on right click), dropdown or static (render into the selected element) 
		items: '> ul', //Can be either a jQuery selector, therefore using markup in the selected node, or a JSON list of menu entries
		appendTo: 'body', //Only in case of context/dropdown - where the actual menu is being appended to,
		exclusive: true, //Defines wether only this menu can be shown at the same time

		width: 180,
		maxHeight: 200, //If height specified and surpassed, scrollbars will be added to the drilldown,
		forceDirection: false,
		direction: undefined,

		hoverClass: 'ui-hover-state',
		hoverClassSecondary: 'ui-component-content',
		nextMenuClass: 'ui-arrow-right-default', // class to style the link (specifically, a span within the link) used in the multi-level menu to show the next level

		//flyout specific
		flyoutDelay: 300,

		//drilldown menu specific
		crossSpeed: 300, // cross-fade speed for multi-level menus
		backLink: true, // in the drilldown-style menu: instead of breadcrumbs, show only a 'back' link,
		backLinkText: 'Back',
		topLinkText: 'All',
		crumbDefaultText: ' ',
		selectCategories: false // set to true if each menu item is a split button where you can choose either the text (to make a selection) or "next" arrow (to navigate)

	}
});

})(jQuery);
